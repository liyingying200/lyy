import datetime
import time
"""
在time模块基础上做进一步的封装
date类：日期类，年月日
time类：时间类，时分秒
datetime类：日期+时间，年月日 时分秒
timedelta类：表示两个datetime对象的差值
tzinfo类: 表示时区的相关信息
"""
# -----------------------date类-----------------------
# 1.使用date类构造一个日期对象
dt = datetime.date(year=2022,month=4,day=13)
print(dt,type(dt))
# 2.today():获取当前日期
td = datetime.date.today()
print(td)
# 3.fromtimestamp(时间戳):将时间戳转化成日期
print(time.time())
tamp = datetime.date.fromtimestamp(time.time()-10*24*60*60)
print(tamp)
# 4.fromordinal(天数)：传入一个天数，返回一个从公元1-1-1开始的日期
gy = datetime.date.fromordinal(10000)
print(gy)
# 5.date类中方法
# 通过创建的日期对象调用方法
print(td.year,td.month,td.day)  # 获取年月日
print(td.timetuple())   # 获取时间元组
print(td.toordinal())   # fromordinal(),逆推算，通过日期推算出从公元1-1-1到今天有多少天
print(td.weekday())     # 周1-周7  是[0,6]区间
print(td.isoweekday())  # 周1-周7  是[1,7]
print(td.isocalendar()) # 返回元组，1.年,2.第几周，3.星期几
print(td.isoformat())   # 返回标准格式  2022-04-13
print(td.strftime("%y-%m-%d"))  # 按照格式进行格式化时间
print(td.replace(year=1111,month=11,day=11))

# --------------------------time类-----------------------
# 1.构造时间
tm = datetime.time(hour=10,minute=10,second=18)
print(tm)
# 2.isoformat():返回标准格式时间
t2 = tm.isoformat()
print(t2)
# 3.strftime():格式化时间
t3 = tm.strftime("%S:%M:%H")
print(t3)
# 4.tzname():返回时区
print(tm.tzname())
# ------------------------datetime类------------------------
# 1.构造一个日期时间
dm = datetime.datetime(year=2022,month=4,day=10,hour=12,minute=10,second=10)
print(dm)
# 2.nom():获取当前这一时刻的时间
nw = datetime.datetime.now()
print(nw)
# 3.fromtimestamp():根据一个时间戳创建一个日期时间
tmp = datetime.datetime.fromtimestamp(15264561111)
print(tmp)
# 4.utcfromtimestamp():国际标准时间
# utcnow（）: 当前的国际标准时间
utc = datetime.datetime.utcnow()
print(utc)
utcf = datetime.datetime.utcfromtimestamp(15264561111)
print(utcf)

# 5.获取其中一部分属性
print(dm.year,dm.month,dm.day,dm.hour,dm.minute,dm.second)
print(dm.time())
print(dm.date())
print(dm.ctime())
print(dm.weekday())
print(dm.timetuple())
# ---------------------timedelta类-----------------------
dt = datetime.datetime.now()
print(dt)
day423 = dt + datetime.timedelta(days=10, hours=1)
print(day423)
day403 = dt - datetime.timedelta(days=10, hours=2, minutes=10)
print(day403)

print("-------------------------------")
birthday = datetime.datetime(year=2003, month=1, day=5).timestamp()
print(birthday)
end_date = datetime.datetime(year=2103, month=10, day=10).timestamp()
print(end_date)
print(end_date - birthday)
while True:
    now = datetime.datetime.now().timestamp()
    time.sleep(1)
    print(f"年轻人, 你还剩下{end_date-now}秒可以挥霍")



