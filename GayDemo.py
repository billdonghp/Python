'''
    多继承
'''


from Person import Person

class Man(Person):
    def tell(self):
        print("孙子，我是%s,今年%d岁，我有%f万元人民币"%(self.name,self.age,self.rmb))

    def roar(self):
        print("大喊一声，孙子你敢答应吗？")

class Woman(Person):
    def tell(self):
        print("大爷，人家是%s,年芳%d有余，人家现有%f万元人民币了呢"%(self.name,self.age,self.rmb))

    def sajiao(self):
        print("人家用小拳拳捶你胸口，打死你打死你!")
#        
class Gay(Woman,Man):
    #已具备了Man，Woman的全部属性和方法
    pass
if __name__ == '__main__':
    m = Man("吏阿龙",40,50.0)
    m.tell()
    m.roar()
    wm = Woman("林妙妙",20,300)
    wm.tell()
    wm.sajiao()

    g = Gay("库克",50,20)
    g.tell()
    g.roar()
    g.sajiao()
