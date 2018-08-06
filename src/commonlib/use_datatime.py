from datetime import datetime,timedelta,timezone
from _datetime import tzinfo

now=datetime.now()
print(now)
print(type(now))

# 用指定日期时间创建datetime
dt=datetime(2018,5,1,12,30,45)
print(dt)

# 把datetime转换为timestamp
print(dt.timestamp())
# timestamp转换为datetime
t=1525149045.0
print(datetime.fromtimestamp(t))

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(now.strftime('%a, %b %d %H:%M'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=1))

#本地时间转换为UTC时间
# 创建时区UTC+8:00
tz_utc_8=timezone(timedelta(hours=8))
print(now)
dt=now.replace(tzinfo=tz_utc_8)
print(dt)