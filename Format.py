'''Format
    str.format()
    基本语法是通过{}和:来代替以前的%
    format函数可以不限个参数、位置可以不按顺序
    通过字典设置参数  **kwagrs
    通过列表索引设置参数 0[0]
    通过传入对象 0.age
'''

print('{:6d}'.format(10))
print('{:0<6d}'.format(11))
print('{:x>6d}'.format(10))
print('{:,}'.format(1000000))
print('{:.2f}'.format(11.8378))
print('{:.0f}'.format(11.8378))
print('{:+.2f}'.format(11.8378))
print('{:.2%}'.format(0.26))

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayPerson(self):
        return '姓名:%s 年龄%d' %(self.name,self.age)
    @staticmethod
    def sDisplayPerson(name,age):
        print( '姓名:%s 年龄%d' %(name,age))
Person.sDisplayPerson('zihao',12)
p = Person('haipeng',39)
print(p.displayPerson())
p1 = {'name':'haipeng','age':39}
p2=['haipeng',39]
#传入对象
print('姓名{0.name} 年龄{0.age}'.format(p))
#传入dictionary
print('姓名{name} 年龄{age}'.format(**p1))
#传入list
print('姓名{0[0]} 年龄{0[1]}'.format(p2))
