'''
变量的作用域
'''
salary = 7000

def raiseSalary(salary):   #salary形参
    salary += salary * 0.08

raiseSalary(salary)

print("raiseSalary加薪后：%d"%(salary))

def raiseSalaryII(salary):   #通过返回值影响
    salary += salary * 0.08
    return salary

salary = raiseSalaryII(salary)

print("raiseSalaryII加薪后：%d"%(salary))


def raiseSalaryIII():
    global salary   #使用全局变量
    salary += salary * 0.1

raiseSalaryIII()

print("raiseSalaryIII加薪后：%d"%(salary))


