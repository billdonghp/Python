'''
    保护存款信息
    为存款信息添加保护，不可以直接访问
    添加密码保护
    
'''

class Person:
    name = "林阿华"
    age = 20

    #私有属性(通过公有属性访问)
    __rmb = 1000

    #公有属性
    def tell(self):
        print("大家好，我是%s"%(self.name))

    def __setRmb(self,rmb):
        self.__rmb = rmb
    #公有属性调用私有属性
    def setRmb(self,rmb):
        pwd =  input("请输入设置密码")
        if pwd == '123456':
            self.__setRmb(rmb)
        else:
            print("您没有权限")
    def getRmb(self):
        pwd =input("请输入查询密码\n")
        if pwd == '123456':
            return self.__rmb
        else:
            return "您没有访问权限"
if __name__ == '__main__':
    p = Person()

    #私有成员不能被直接访问
    #print(p.__rmb)
    p.tell()
    p.setRmb(500)
    rmb = p.getRmb()

    print("我的存款是：",rmb)
