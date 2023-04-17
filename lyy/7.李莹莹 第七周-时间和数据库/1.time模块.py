import time
"""
time模块：用来获取时间，操作时间
"""
# 1.time():可以获取当前时间戳
# 时间戳：就是从1970年1月1日0:0:0开始到现在这一刻的总秒数，浮点数，小数点后精准7位
tt = time.time()
print(tt)
# 2.localtime():获取本地的时间，是一个时间元组
# tm_year= 2022,tm_mday=12,tm_hour=11,tm_min=23,tm_sec=32,tm_wday=1,tm_yday=102,tm_isdst=0
ltime = time.localtime()
print(ltime)
print("年",ltime.tm_year,"月",ltime.tm_mon,"这个月第几日",ltime.tm_wday)
# tm_wday:本周第几日，周一是0，总共（0-6）
print("这年第几日",ltime.tm_yday,"这周第几日",ltime.tm_wday)
# tm_isdst   是否为夏令时，值有：1（夏令时）、0（不是夏令时）、-1（未知），默认 -1
print(ltime.tm_isdst)
# 3.asctime():获取格式化的本地时间
asc = time.asctime()
# tue  apr  12  11:30:08  2022
# 星期  月  日  时：分：秒  年
print(asc)
# 处理成中国人喜欢的
tlist = asc.split(" ")
print(tlist)
week = tlist[0]
year = tlist[-1]
month = tlist[1]
day = tlist[2]
t = tlist[3].split(":")
hour = t[0]
minu = t[1]
sec = t[-1]
print(f"{year} 年 {month} 月 {day} 日 {hour} : {minu} : {sec} 星期{week}")
# 4.strftime():将时间元组格式化成想要的格式
strtime = time.strftime("%Y-%m%d %H:%M:%S",time.localtime())
print(strtime)
"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23)
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%s 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""

# 5.strptime():将时间字符串，转换成时间元组
strp = time.strptime("11-11-2011 11:11:11","%m-%d-%Y %H:%M:%S")
print(strp)
# 6.perf_counter():获取cpu界别的精准时间计算，可以计算程序运行时间
pc = time.perf_counter()
print(pc)
strt = time.perf_counter()
# for i in range(1000000):
#    print(i)
end = time.perf_counter()
print(end - strt)
# 7.sleep():让程序睡一会
# time.sleep(3)
print("程序继续运行")
# 8.ctime():返回当前时间的字符串形式，表示为易读的时间结果
ctime = time.ctime()
print(ctime)
# 9.gmtime():获取当前时间，表示为计算机可处理的时间格式，时间元组
gm = time.gmtime()
print(gm)
