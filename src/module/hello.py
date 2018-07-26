'a test module'

__author__='huowolf'

import sys

def test():
    #argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    if(len(args)==1):
        print("hello,world!")
    elif(len(args)==2):
        print("hello,%s" % args[1]) 
    else:
        print("Too many arguments")
       
#if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__=='__main__':
    test()
        