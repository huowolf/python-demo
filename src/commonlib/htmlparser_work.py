#找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，
#然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
#===============================================================================
# event:
# <h3 class="event-title"><a href="/events/python-events/745/">PyCon Korea 2018</a></h3>
# time:
# <time datetime="2018-08-15T00:00:00+00:00">15 Aug. &ndash; 20 Aug. 
# <span class="say-no-more"> 2018</span></time>
# location:
#  <span class="event-location">Seoul, South Korea</span>
#===============================================================================
 
from html.parser import HTMLParser
from urllib import request

class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_title=False
        self.is_location=False
        self.is_time=False
        self.times=[]
        self.event={}
        self.eventList=[]
    
    #遇到开始标签时，设置各个标志位为True    
    def handle_starttag(self, tag, attrs):
        if('class','event-title') in attrs:
            self.is_title=True
        if('class','event-location') in attrs:
            self.is_location=True
        if tag=='time':
            self.is_time=True   
            
    #遇到结束标签时，设置各个标志位为False，以便进行下一次的解析 
    def handle_endtag(self, tag):
        if tag=='h3':
            self.is_title=False
        if tag=='span':
            self.is_location=False
        if tag=='time':
            #完成event[time]属性的组装
            self.event['time']=' '.join(self.times)                 
            #重置数据
            self.is_time=False
            self.times=[]
            
        #当遇到li结束标签时,将event对象放入eventList
        if tag=='li':
            #如果event对象不为空，将event对象放入eventList(去掉那些无用的li标签的解析)
            if self.event:
                self.eventList.append(self.event)
                #同时初始化event
                self.event={}


            
    #解析数据
    #将各个数据组装成一个event(dict)
    def handle_data(self, data):
        if self.is_title:
            self.event['title']=data
        if self.is_location:
            self.event['location']=data
        if self.is_time:
            self.times.append(data)
            
    #统一打印eventList对象
    def showEvent(self):
        print(self.eventList)
        for event in self.eventList:
            print('title:',event['title'])
            print('location:',event['location'])
            print('time:',event['time'])
            print('------------------------')
            
with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read()
    req =data.decode('utf-8')
    
parser = MyHtmlParser()
parser.feed(req)
parser.showEvent()
        