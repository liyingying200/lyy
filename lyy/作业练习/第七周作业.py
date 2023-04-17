# 利用os模块, 获取到电脑c盘下所有的文件名字, 并经过正则对文件名进行匹配,文件结尾是.txt的文件名进行保留, 写入一个文件:  myfile.txt中, 每个文件名独占一行
import os
import re
aa = os.walk(r"C:\Users")
list1 =[]
for i in aa:
    for o in i:
        if isinstance(o,str):
            if o:
                aaa = re.findall(pattern="(.*.txt)$", string=o)
                list1.append(aaa)
        if isinstance(o,list):
            for v in o:
                aaa = re.findall(pattern="(.*.txt)$", string=v)
                list1.append(aaa)
for s in list1:
    if s == []:
        while [] in list1:
            list1.remove(s)
str1 = str(list1)
str2 = str1.replace("[","").replace("]","").replace(",","\n")
ff = open("myfile.txt","w",encoding="utf-8")
ff.write(str2)
ff.close()