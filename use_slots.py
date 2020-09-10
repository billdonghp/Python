class Person(object):
    pass
#instance实例
p = Person()

#给实例绑定一个属性
p.age = 12
print(p.age)

#定义一个函数作为实例方法
def setName(self,name):
    self.name = name

def setScore(self,score):
    self.score=score

    
#给实例绑定一个方法
from types import MethodType
p.setName = MethodType(setName,p)

p.setName('dong')
print(p.name)

#另一个实例不起作用
p2=Person()
#print(p2.name)

#给class绑定方法

Person.setScore = setScore

p.setScore(99)
print('p_score: ',p.score)

p2.setScore(60)

print('p2_score: ',p2.score)


'''
   使用__slots__ 限制添加属性
   对当前类实例起作用，对继承子类是不起作用的
'''
class Animal(object):
    __slots__=('name','age')

a=Animal()
a.name='dog'
print(a.name)
#AttributeError: 'Animal' object has no attribute 'sex'
a.sex="FM"

print(a.sex)


