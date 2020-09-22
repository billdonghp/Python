def yy():
    year = eval(input("input year\n"))
    yy = ["猴", "鸡", "狗", "猪", "鼠", "牛", "虎", "兔" "龙", "蛇", "马", "羊"]
    result = yy[year % 12]
    print("%d年是%s年" % (year, result))


if __name__ == "__main__":
    yy()