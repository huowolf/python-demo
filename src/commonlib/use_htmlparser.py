from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    #处理开始标签，比如<xx>
    def handle_starttag(self, tag, attrs):
        print('starttag:<%s>' % tag)
        
    #处理结束标签，比如</xx>
    def handle_endtag(self, tag):
        print('endtag:</%s>' % tag)

    #处理自闭合标签
    def handle_startendtag(self, tag, attrs):
        print('startendtag:<%s/>' % tag)

    #处理数据，就是<xx>data</xx>中间的那些数据
    def handle_data(self, data):
        print('data:%s' % data.strip())

    #处理注释
    def handle_comment(self, data):
        print('<!--', data, '-->')

    #处理一些特殊字符，以&开头的，比如 &nbsp
    def handle_entityref(self, name):
        print('&%s;' % name)

    #处理特殊字符串，就是以&#开头的，一般是内码表示的字符
    def handle_charref(self, name):
        print('&#%s;' % name)
        
        
if __name__ == '__main__':
    parser = MyHtmlParser()
    
    with open('demo.html') as f:
        content = f.read()
        
    parser.feed(content)