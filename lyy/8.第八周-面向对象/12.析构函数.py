# __del__方法:类魔法方法，Python具有垃圾对象回收机制，当某个示例对象所有引用被清除后，所占内存空间自动释放，Python提供的__del__()会处理
import time
name = "司马迁"
print(name)
del name
# print(name)
# 定义类
class King():

    def __init__(self, name):
        self.name = name
        print("对象实例化，被调用")

    def __del__(self):
        #
        print("实例对象%s被删除会调用这个del函数" % self.name)

if __name__ == '__main__':
    # 实例化对象
    qsh = King(name="嬴政")
    # 手动删除对象
    del qsh   # 执行del语句，对象会调用__del__函数删除这个对象
    time.sleep(3)
    print("结束程序")
