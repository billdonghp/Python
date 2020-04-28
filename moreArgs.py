
'''
 位置参数
 不定长位置参照  *args
 定长关键字
 不定长关键字  **kwargs
 返回值return

 元组：tuple
'''

def moreArgs(sender,toWhom,count,*args,city="北京",date="2018-7-30",**kwargs):
    print("Sender:%s"%(sender))

    print("toWhom:%s于%s在%s接收到"%(toWhom,city,date))

    for i in range(count):
        print("我想对你说的话：...")
        print("我不想对你说的话：...")
        print("未来他想对你说的话：...")

    print("点赞的人:",args)

    print("备注信息：",kwargs)

    return "哦",666,"你也懂了吧！"


#result = moreArgs("林阿华","綦书朋",1,"林伟键","于雪梅","王士勇",city="南京",supper="天王盖地虎",Manger="Haipeng Dong")


#print("返回值:",result)


r1,r2, r3 = moreArgs("林阿华","綦书朋",1,"林伟键","于雪梅","王士勇",city="南京",supper="天王盖地虎",Manger="Haipeng Dong")



print("返回值:",r1,r2,r3)
