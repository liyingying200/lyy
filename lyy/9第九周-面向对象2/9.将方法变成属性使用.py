class Student():
    def __init__(self,id,name,sex,phone):
        self.id = id
        self.name = name
        self.sex = sex
        self.__phone = phone

    @property   # 将这个方法调用方式变成属性方式获取
    def phone(self):
        # 类的内部可以调用私有属性
        return self.__phone
    @phone.setter
    def phone(self,p):
        # 内部修改私有属性
        self.__phone = p

if __name__ == '__main__':
    sun = Student(id = "123456",name= "孙铭辰",sex = "男",phone="123457899")
    # 通过方法获取修改私有属性
    # print(sun.get_hidden())
    # sun.set_hidden(p="123889004")
    # print(sun.get_hidden())
    # 公有属性获取修改
    print(sun.name)
    sun.name = "孙明晨"
    print(sun.name)
    # 让方法变成属性调用方式
    cai = Student(id = "1234567",name= "蔡萌",sex = "女",phone="123456769")
    print(cai.phone)
    cai.phone = "874209857"
    print(cai.phone)
