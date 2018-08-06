import subprocess

print('nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)


#---------------------------
#子进程可以通过communicate()方法输入
#q=mx(邮件交换记录)
print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# The optional "input" argument should be data to be sent to the
# child process (if self.universal_newlines is True, this should
# be a string; if it is False, "input" should be bytes), or
# None, if no data should be sent to the child.

#其中universal_newlines(通用换行符'\n'),该参数默认初始化是Fasle
#故input参数默认接受的是byte数组

# communicate() returns a tuple (stdout, stderr).  These will be
# bytes or, if self.universal_newlines was True, a string.
output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code',p.returncode)