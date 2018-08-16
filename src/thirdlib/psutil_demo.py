#psutil = process and system utilities
#获取系统信息
import psutil

#CPU逻辑数量
print(psutil.cpu_count())

# CPU物理核心
print(psutil.cpu_count(logical=False)) 

#统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())