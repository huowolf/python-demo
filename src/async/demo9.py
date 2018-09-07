import requests
import time
import multiprocessing
 
start = time.time()
 
def request(_):
    url = 'http://127.0.0.1:5000'
    print('Waiting for', url)
    result = requests.get(url).text
    print('Get response from', url, 'Result:', result)
    

if __name__ == '__main__':
    #freeze_support()
    cpu_count = multiprocessing.cpu_count()
    print('Cpu count:', cpu_count)
    pool = multiprocessing.Pool(cpu_count)
    # 第一个参数是函数，第二个参数是一个迭代器，将迭代器中的数字作为参数依次传入函数中
    pool.map(request, range(50))
    pool.close()
    pool.join()
    end = time.time()
    print('Cost time:', end - start)