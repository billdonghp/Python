class MyClass:
    name = "张三"

    def tell(self):
        print(self.name)

    def setName(self, name):
        self.name = name

    # 类方法
    @classmethod
    def cMethod(cls):
        print("classmethod\n")
        print(cls)
        print(MyClass.name)

    # 静态方法
    @staticmethod
    def sMethod():
        print("staticmethod\n")
        print(MyClass.name)


if __name__ == '__main__':
    mc = MyClass()

    mc.tell()

    mc.setName("李四")

    mc.tell()
    # 类方法不取实例中的setName后的name
    mc.cMethod()

    mc.sMethod()

    print("----------")

    MyClass.cMethod()

    MyClass.sMethod()
