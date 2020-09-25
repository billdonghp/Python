'''
    类测试
'''

# import Person.Person

# from模块import 成员(变量、函数、类)
from Person import Person
import calendar


# 水仙花数 也称超完全数字不变数
def narcissisticNumber():
    result = []
    for x in range(100, 1000):
        if (x // 100)**3 + ((x // 10) % 10)**3 + (x % 10)**3 == x:
            result.append(x)
    print(result)


if __name__ == '__main__':
    # p = Person("尔阿康", 30, 1000)
    # p.tell()
    # narcissisticNumber()
    print(calendar.month(2020, 10))
