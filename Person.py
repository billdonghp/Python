'''
 封装人员信息
     Person类
'''


class Person:
    #属性
    name = "林阿华"
    age = 20
    rmb = 50.0
    
    #构造方法  外界创建类的实例时调用
    #构选方法是初始化实例属性的最佳时机
    def __init__(self,name,age,rmb):
        print("老子被创建了")
        self.name = name
        self.age = age
        self.rmb = rmb
    #
    def __str__(self):
        return "{name:%s,age:%d,rmb:%s}"%(self.name,self.age,format(self.rmb,".2f"))
    
    #方法或函数
    #self 类的实例
    #自我介绍方法
    def tell(self):
        
        print("我是%s,我%d岁了，我有%s元"%(self.name,self.age,format(self.rmb,".2f")))

if __name__ =='__main__':
    p = Person("易中天",50,100000.0)
    p.tell()

    print(p)
