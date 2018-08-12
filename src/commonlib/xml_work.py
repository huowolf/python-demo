#请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
#https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml
#返回如下格式的数据
#===============================================================================
# return {
#         'city': '?',
#         'forecast': [
#             {
#                 'date': '2017-11-17',
#                 'high': 43,
#                 'low' : 26
#             },
#             {
#                 'date': '2017-11-18',
#                 'high': 41,
#                 'low' : 20
#             },
#             {
#                 'date': '2017-11-19',
#                 'high': 43,
#                 'low' : 19
#             }
#         ]
#     }
#===============================================================================
#观察XML格式，city信息在yweather:location标签中
#天气信息在yweather:forecast标签中

from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherSaxHandler(object):
    weather={'forecast':[]}
    # name 是标签名，attrs 是一个 dict，返回标签的属性
    def start_element(self,name,attrs):
        if name=='yweather:location':
            self.weather['city']=attrs['city']
        elif name=='yweather:forecast':
            self.weather['forecast'].append({
                    'date':attrs['date'],
                    'high':attrs['high'],
                    'low':attrs['low'],
                })

def parseXml(xml_str):
    handler=WeatherSaxHandler()
    parser=ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)
    return handler.weather
    
    

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'