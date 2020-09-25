import time


def timeDemo():
    print(time.time())  # 时间戳
    print(time.mktime(time.localtime()))  # struct_time元组转换为 Timestamp 时间戳
    print(time.mktime((2020, 9, 25, 11, 20, 20, 4, 269, 0)))
    print('--' * 10, 'struct_time')
    print(time.localtime())  # struct_time元组
    print(time.gmtime())  # UTC时区（0时区）的struct_time
    print(time.strptime('2020-09-23 07:59:57',
                        '%Y-%m-%d %X'))  # 时间字符串格式化为struct_time元组
    print('--' * 10, 'string')
    print(time.ctime(time.time()))  # Timestamp  => 字符串'%a %b %d %H:%M:%S %Y'
    print(time.asctime(
        time.localtime()))  # struct_time => 字符串'%a %b %d %H:%M:%S %Y'
    print(time.strftime('%a %b %d %H:%M:%S %Y',
                        time.localtime()))  # struct_time元组格式化为字符串
    # %a星期 %b 月（%A%B%完整星期、月）  %d：mday  %H  hour %M 分 %S 秒 %X=%H:%M:%S


if __name__ == "__main__":
    timeDemo()