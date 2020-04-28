'''九九乘法表'''

for i in range(1,10):
    for j in range(1,i+1):
        result = format(i*j,">2d")

        print("%d*%d=%s"%(j, i,result),end="  ")
    print("\n")
