'''
字符串操作符  + *
字符串的长度  len
比较字符串大小
字符串截取 [:] [0:] 
判断有无子串 in not in 
查找子串出现的位置 find()  index() 不存在的话报错
encode,decode
replace(old,new,count)、count(sub,start,end)
isdigit()、startswith
split、join  '-'.join('我爱你中国')
隔位截取str1[::2]  = str1[0:-1:2] start 和end不写时为全部；step=2 如果 step为负数时，倒序截取； 
'''
str1 = 'hello'
a = 'a'
b = 'b'


def stringEncode(str):
    myBytes = str.encode(encoding='utf-8')
    return myBytes


if __name__ == "__main__":
    print(len(str1))
    print(a < b)
    print('中国' < '美国')  #utf-8中 美比中大
    print(str1[2:])
    print(str1.upper())
    sEncode = stringEncode('我爱你中国')
    print(sEncode.decode(encoding='utf-8'))
    print(str1.find('7'))
    print(str1[::-1])
    pass
