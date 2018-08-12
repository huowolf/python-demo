import xml.etree.ElementTree as ET
import sys
from xml.dom import minidom
#将XML文档解析为树（tree）
#------------------------------
#加载文档
tree=ET.ElementTree(file='doc.xml')
#获取根元素
root = tree.getroot()
#查看根元素属性（根元素并没有属性）
print(root.tag,root.attrib)
#根元素也具备遍历其直接子元素的接口
for child_of_root in root:
    print(child_of_root.tag,child_of_root.attrib)
    
#还可以通过索引值来访问特定的子元素
print(root[0].tag,root[0].text.strip())
#-------------------------------------

print('-------------------------')

#查找需要的元素
#--------------------------------
#遍历XML文档中所有元素的最简单方法
for elem in tree.iter():
    print(elem.tag,elem.attrib)

print('-------------------------')
#iter方法可以接受tag名称，然后遍历所有具备所提供tag的元素
for elem in tree.iter(tag='branch'):
    print(elem.tag,elem.attrib)
#-------------------------------------

#支持通过XPath查找元素
#-----------------------------------
#Element对象中有一些find方法可以接受Xpath路径作为参数，find方法会返回第一个匹配的子元素，
#findall以列表的形式返回所有匹配的子元素, iterfind则返回一个所有匹配元素的迭代器（iterator）

#查找branch元素之下所有tag为sub-branch的元素
for elem in tree.iterfind('branch/sub-branch'):
    print(elem.tag,elem.attrib)
#查找所有具备某个name属性的branch元素
for elem in tree.iterfind('branch[@name="release01"]'):
    print(elem.tag,elem.attrib)
#-----------------------------------

#构建XML文档
#------------------------------------
#1.读取一个XML文档，进行修改，然后再将修改写入文档
root=tree.getroot()
del root[2]
root[0].set('foo','bar')
for subelem in root:
    print(subelem.tag,subelem.attrib)

#将修改后的树重新写入至文件中
#tree.write('doc_1.xml')
#将修改后的树重新写入至标准输出
tree.write(sys.stdout,encoding='unicode')
#tree.write(sys.stdout.buffer)

#从头构建一个完整的文档

#格式化输出xml文件  
#使用minidom模块来完成格式化输出
def write_pretty(root,output_path):       
    rough_string = ET.tostring(root, 'utf-8')  
    xml_write = minidom.parseString(rough_string)  
    with open(output_path, 'w') as handle:
        xml_write.writexml(handle, addindent='  ', newl='\n', encoding='utf-8'); 

a=ET.Element('elem')
c=ET.SubElement(a,'child1')
c.text='some text'
d=ET.SubElement(a,'child2')
b = ET.Element('elem_b')
root=ET.Element('root')
root.extend((a,b))
tree=ET.ElementTree(root)

tree.write(sys.stdout,encoding='unicode')
#格式化输出
write_pretty(root, 'build.xml')

#------------------------------------

#利用iterparse解析XML流