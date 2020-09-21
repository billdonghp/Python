# 生成列表的方法：
def createList():
    # 1.普通创建
    mlist = []
    mlist = [1, 2, 3, 'complex', True, 5 + 6j]
    # 2.推导式创建
    mlist = [c for c in 'hello']
    mlist = ['$' + c for c in 'hello']
    mlist = ['$' + c for c in 'hello' if c != 'e']
    return mlist


# 访问元素
def visitList():
    print(len(mlist))
    print(mlist[2])


# 遍历元素
def iteraterList():
    for i in mlist:
        print(i)


# 修改元素
def editList():
    mlist[2] = 'banana'
    mlist.extend(ylist)


# 删除元素
def delItem():
    del mlist[3]
    mlist.clear()
    # del mlist  #内存中删除


# 操作符 + *
def operatorsList():
    print(mlist + dlist)
    print(ylist * 2)
    print(1 in ylist)
    print(5 not in ylist)


# 截取
def subList():
    print(mlist[0:3])  # 含头不含尾
    print(mlist[0:-3])
    print(mlist[3:])
    print(mlist[:-3])
    print(mlist[:])
    print(mlist[::2])
    print(mlist[::-2])
    print(mlist[::-1])


# 嵌套列表
def nestedList():
    ilist = [
        mlist,
    ]
    ilist.append(ylist)
    ilist.append('count')
    print(ilist[0][3])


# 内建函数 len(list)、max(list)、min(list)、list(iterable)  builtins.py
def builtinFuncs():
    print(len(dlist))
    print(max(dlist))
    print(min(dlist))
    print(dlist)
    print(list('hello'))  # 将iterable（容器或字符串）类型转换为列表
    print(list((1, 2, 3)))


# list常用函数
def listFuncs():
    # 返回值为int
    print(mlist.count('apple'))
    print(mlist.index('apple'))
    print(mlist.index('apple', 4))
    print(mlist.index('apple', 5, -1))
    # 返回值为item
    print(mlist.pop())
    print(mlist.pop(3))
    # 返回值为None
    mlist.append('ThinkPd')
    mlist.remove('google')
    mlist.reverse()
    mlist.sort()
    print(mlist.copy())
    mlist.clear()


# 逆向遍历
def reversedIterater():
    for i in reversed(mlist):
        print(i)


# 组合遍历
def zipList():
    for i, y in zip(dlist, ylist):
        print('No.%d:%s' % (i, y))


if __name__ == "__main__":
    mlist = [
        'google', 'microsoft', 'huawei', 'apple', 'apple', 'apple', 'tencent',
        'alibaba'
    ]
    ylist = ['百度', '新浪', '茅台']
    dlist = list(range(3))
    # visitList()
    # iteraterList()
    # editList()
    # delItem()
    # operatorsList()
    # subList()
    # nestedList()
    # builtinFuncs()
    # listFuncs()
    # zipList()
    # reversedIterater()
    print(mlist)
