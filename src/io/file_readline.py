#按行读取文件的方法：
import codecs
with codecs.open('test.txt') as file:
    for line in file.readlines():
        print(line.strip())# 把末尾的'\n'删掉
    