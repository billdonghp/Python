class Animal():
    pass


class Person(object):
    name = '张三'
    age = 34
    rmb = 10.0

    # 构造方法 Constructor
    def __init__(self, name, age, rmb):
        self.name = name
        self.age = age
        self.rmb = rmb

    # toString方法
    def __str__(self):
        return '{name: %s, age: %d, rmb: %.2f}' % (self.name, self.age,
                                                   self.rmb)

    # 比较 __ge__ __eq__ __len__
    # __add__ __sub__ __mul__ __truediv__  __divmod__ __mod__ __pow__
    def __gt__(self, other):
        if not isinstance(other, Person):
            raise TypeError(' > 运算对象是Person')
        elif self.age > other.age:
            return True
        else:
            return False


if __name__ == "__main__":
    p1 = Person('李四', 36, 20.0)
    p2 = Person('王王', 35, 3.0)
    a = Animal()
    print(p1)
    try:
        p1 > a
    except Exception as e:
        print(repr(e))
    print(p1 > p2)
