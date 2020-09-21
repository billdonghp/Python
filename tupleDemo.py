'''
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''


# 创建
def createTuple():
    mtup = ()
    mtup = (1, )  # 单个元素后面加逗号
    mtup = (1, None, True, 3.14, 'hello')
    mtup = 1, None, True, 3.14, 'hello'  # 任意无符号的对象，以逗号隔开，默认为元组
    print(mtup)


# 访问元素
def visitTuple():
    print(mtup[2])


# 删除
def delTuple():
    del mtup
    #print(mtup)


# 操作符
def operatorsTuple():
    print(mtup * 2)
    print(mtup + ytup)
    print(3.14 in mtup)
    print(3.14 not in mtup)


# 截取
def subTuple():
    print(mtup[:])
    print(mtup[0:3])
    print(mtup[:3])
    print(mtup[3:])
    print(mtup[2:-1])  # 含头不含尾


# 遍历
def iteraterTuple():
    for i in mtup:
        print(i)


# 内建函数
def builtinsFuncs():
    print(len(mtup))
    print(max(ytup))
    print(min(ytup))
    print(tuple(['java', 'c++', 'python']))


# Tuple函数
def tupleFuncs():
    print(mtup.count(3.14))
    print(mtup.index(3.14))


if __name__ == "__main__":
    mtup = (1, None, True, 3.14, 'hello')
    ytup = tuple('hello')
    # createTuple()
    # visitTuple()
    # delTuple()
    # operatorsTuple()
    # subTuple()
    # iteraterTuple()
    # builtinsFuncs()
    # tupleFuncs()
