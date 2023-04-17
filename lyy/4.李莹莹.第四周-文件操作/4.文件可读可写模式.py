"""
1.需要文件存在，不存在会报错，打开后光标在开头
r:只读模式
r+:可读可写,打开文件，原来内容不会清空
rb:只读二进制数据文件，和r是相同
rb+:读写二进制文件，和r+是相同的
2.不需要文件存在，不存在会创建，每次打开清空文件
w:只写模式
w+:可写可读
wb: 写入二进制文本
wb+: 写读二进制文本
"""
frj = open(file="将进酒.txt",mode="r+",encoding="utf-8")
print(frj.readable())
print(frj.writable())
# 可以读取
text = frj.read()
print(text)
# 写入
frj.write("\n人生得意须尽欢，莫使金樽空对月")
frj.seek(0)
print(frj.readlines())
frj.close()

fwj = open("阿房宫赋.txt",mode="w+",encoding="utf-8")
print(fwj.readable())
print(fwj.writable())
# 可以写入，写入后光标移动到末尾
fwj.write("六王毕，四海一，蜀山兀，阿房出")
# 可以读取
fwj.seek(0)
print(fwj.read())
fwj.close()

fb = open("apple.png","rb")
print(fb.read())
# fwb = open("red_apple.jpg","wb")
# fwb.write(fb.read())
# fwb.close()
fb.close()
"""
练习：使用w+模式打开一个文件a.txt，水仙花数 1000以内的数字写入文件，回文数，五位数，写入文件，写入时候，分类写入，可以读取出来
"""
wj = open("a.txt", "w+", encoding="utf-8")
for wq in range(1000):
    ge = wq % 10
    shi = wq // 10 % 10
    bai = wq // 100
    if ge**3 + shi**3 + bai**3 == wq:
        wj.write("水仙花数"+str(wq) + "\n")
for i in range(10000, 100000):
    s = str(i)
    if s[0] == s[-1] and s[1] == s[-2]:
        wj.write("回文数" + str(i) + "\n")
wj.close()


