def searcher():
    list = ["付瑾","孙松海","姜晓毅","程国前","林伟健","董海朋","王士勇","綦书朋","于艳妮","于雪梅","杨斌","金鹏飞","刘正平","孙晓云"]

    goddes = input("input goddes:\n")

    index = 0

    searchOk = False

    for x in range(len(list)):
        temp = list[x]

        if temp == goddes:

            searchOk = True
            index = x

    if not searchOk:
        print("未找到此人")

    else:
        print("您找的人：%s在第%d号"%(goddes,index))


searcher()
