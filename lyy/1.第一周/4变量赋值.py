# 变量赋值
# 1.给单个变量赋值，使用 = ：赋值等号
# == :判断左右两边相等
str_name = "天王星，冥王星"
print(str_name)
number = 99999
print(number)
pi= 3.1415626
print(pi)
bl = True
print(bl,type(bl))
# 2.多个变量赋值相同的值
a = 10
b = 10
c = 10
# 使用连等号
x = y = z = 100
print(x,y,z)
name = "海绵宝宝"
print(name)
ab = cd = w = "派大星"
print(ab,cd,w)
# 3. 多个变量赋值不同的值
o = 6
p = 7
q = 8
n, m = 8000, 9000
print(n,m)

# 4.两个变量交换数据
zhang = "宝马"
wang = "比亚迪"
print(zhang, wang)
# 可以利用第三个变量
zj = zhang  # zj = zhang = "宝马"
print(zj)
zhang = wang
wang = zj
print(zhang,wang)
# python中提供
zhang,wang = wang,zhang
print(zhang,wang)
# q= "貂蝉"  w = “昭君” r = “甄姬”
#  交换数据，q = "昭君"  r = "貂蝉"  w = "甄姬"
q = "貂蝉"
w = "昭君"
r = "甄姬"
print(q,w,r)
q ,r = r, q
print(q,r)
q,w = w, q
print( q,r,w)



