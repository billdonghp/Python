def leapYear():
    year = eval(input("input year\n"))
##    print(year%4)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("%dYear is leap year"%(year))
    else:
        print("%dYear is not leap year"%(year))


leapYear()

