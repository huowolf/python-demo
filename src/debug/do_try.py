try:
    print('try...')
    #r=10/0
    #r=10/2
    r=10/int('a')
    print('result:',r)
    
    #可以有多个except来捕获不同类型的错误

except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)

#当没有错误发生时，会自动执行else语句
else:
    print('no error!')
finally:
    print('finally')
print('END')
    

