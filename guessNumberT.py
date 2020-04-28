def guessNumberT():
    import random
    answer = random.randint(1,1000)

    myGuess = None

    while myGuess != answer:
        myGuess = eval(input("input number:(1~1000)\n"))

        if myGuess == -1:
            print("不玩了，回家吃饭！")
            break

        if myGuess >1000 or myGuess <1:
            print("眼瞎啊，输对了")
            continue

        if answer > myGuess:
            print("输小了")

        elif answer < myGuess:
            print("输大了")

        else:
            print("恭喜！答对了！")

    print("答案是：%d"%(answer))


guessNumberT()
