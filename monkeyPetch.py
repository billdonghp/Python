'''猴子吃桃的
    猴子接若干个桃子，第一天吃了一半之后又吃了一个，第二天吃了剩余的一半后又吃了一个
    按此方法吃到第十天的时候剩下一天，问猴子摘多少桃子
'''


def monkeyPetch():
    sum = 1
    for i in range(9):
        sum = (sum + 1) * 2
    return sum

def eatPeach():
    peach = 1
    print('猴子第10天还剩下1个桃子')
    for i in range(9,0,-1):
        peach = (peach+1)*2
        print('猴子第%d天还有%d个桃子'%(i,peach))
    print('猴子一共摘了%d个桃子'%peach)

def whilePeatch():
    sum = 1
    days = 1
    while days < 10:
        sum = (sum+1) * 2
        days = days + 1
    return sum

if __name__ == "__main__":
    # print(monkeyPetch())
    # print(whilePeatch())
    #eatPeach()
    