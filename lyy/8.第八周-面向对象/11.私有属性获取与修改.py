# 定义类
class Seafood(object):

    def __init__(self, name, sex, work, job):
        self.name = name    # 共有属性
        self.sex = sex
        self._work = work    # 保护属性
        self.__job = job      # 私有属性，类外访问不到，类内可以调用

    def get_hidden(self):
        """获取私有属性方法"""
        return self.__job
    def set_hidden(self,job):
        """修改私有属性方法"""
        self.__job = job

if __name__ == '__main__':
    hmbb = Seafood(name="海绵宝宝", sex="男", work="厨师", job="抓水母")
    print(f"{hmbb.name}是{hmbb.sex}孩子,职业{hmbb._work}")
    # 通过调用获取私有属性的方法来查看私有属性
    j = hmbb.get_hidden()
    print(f"{hmbb.name}是{hmbb.sex}孩子,职业{hmbb._work},爱好{j}")
    # 再实例化章鱼哥
    zyg = Seafood(name="章鱼哥", sex="男", work="收银员", job="吹竖笛")
    print(f"{zyg.name}是{zyg.sex}孩子,职业{zyg._work},爱好{zyg.get_hidden()}")
    # 修改这个私有属性，通过修改私有属性方法进行修改
    zyg.set_hidden(job="弹钢琴")
    print(f"{zyg.name}是{zyg.sex}孩子,职业{zyg._work},爱好{zyg.get_hidden()}")
    # 蟹老板
    xlb = Seafood(name="蟹老板", sex="男", work="老板", job="数钱")
    print(f"{xlb.name}是{xlb.sex}孩子,职业{xlb._work},爱好{xlb.get_hidden()}")
    # 珊迪
    sd = Seafood(name="珊迪", sex="女", work="科学家", job="空手道")
    print(f"{sd.name}是{sd.sex}生,职业是{sd._work},爱好{sd.get_hidden()}")