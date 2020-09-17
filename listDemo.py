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


'''
内建函数 len(list)、max(list)、min(list)、list(iterable)
'''

if __name__ == "__main__":
    mlist = ['google', 'microsoft', 'huawei', 'apple', 'tencent', 'alibaba']
    ylist = ['百度', '新浪', '茅台']
    dlist = list(range(10))
    # visitList()
    # iteraterList()
    # editList()
    # delItem()
    # operatorsList()
    # subList()
    # nestedList()

    print(len(dlist))
    print(max(dlist))
    print(min(dlist))
    print(dlist)
    # print(mlist)
