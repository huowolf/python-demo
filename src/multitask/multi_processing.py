from multiprocessing import Process

import os

#子进程要执行的代码
def run_proc(name):
    print('run child process  %s (%s)' % (name,os.getpid()))
    print('child process will end')
    

if __name__ == '__main__':
    print('parent process %s ' % os.getpid())
    
    #创建子进程时，需要传入一个执行函数和函数的参数
    p=Process(target=run_proc,args=('test',))
    print('child process will start ')
    p.start()
    
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('parent process end')