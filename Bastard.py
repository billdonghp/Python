'''
有人的地方就有坏蛋
坏蛋类用以存储坏蛋的信息
class Bastard(Person) 继承Person类
super().__init__(name,age,rmb)
类的继承和方法覆写
'''
from Person import Person
class Bastard(Person):

    #恶习
    bayHobby = None

    #覆写父类的构造方法
    def __init__(self,name,age,rmb,badHobby):
        #调用父类构造方法
        super().__init__(name,age,rmb)
        print("混蛋的初始化")
        self.badHobby = badHobby

    #覆写父类的方法
    def tell(self):
        print("我是你老子：%s,此树是我裁，此路是我开，要想过此路留下买路财!"%(self.name))

    #设置器
    def setBadHobby(self,badHobby):
        self.badHobby = badHobby

    def getBadHobby(self):
        return self.badHobby
    #特有方法:作恶
    def doBadThings(self):
        print("铁牛专好%s"%(self.badHobby))

if __name__ == '__main__':
    b = Bastard("单阿信",35,500,"喝酒、杀人!")
    b.tell()
    b.doBadThings()
    b.setBadHobby("杀进东京，夺了鸟位")
    print(b.getBadHobby())
