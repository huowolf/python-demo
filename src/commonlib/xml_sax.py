from xml.parsers.expat import ParserCreate

class DefualtSaxHandler(object):
    def start_element(self,name,attr):
        print('sax:start element:%s,attrs:%s' %(name,str(attr)))
    
    def end_element(self,name):
        print('sax:end element:%s' % name)
        
    def char_data(self,text):
        print('sax:char data:%s' % text)
        
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
        
handler=DefualtSaxHandler()
parser=ParserCreate() 
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

#===============================================================================
# #最简单也是最有效的生成XML的方法是拼接字符串
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append('some & data')
# L.append(r'</root>')
# print(''.join(L))
#===============================================================================
