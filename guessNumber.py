def guessNumber():
    import random
    answer = random.randint(1,1000)

    myGuess = None

    while answer != myGuess :
        myGuess = eval(input("input number"))

        if answer > myGuess:
            print("小了")
        elif answer < myGuess:
            print("大了")
        else:
            print("猜对了")
    print("生成随机数为%d"%(answer))


guessNumber()
