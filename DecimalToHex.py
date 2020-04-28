def decimalToHex(decimal):
    length = len(str(decimal))
    #print(length)
    hexLength = 0
    result = "0x"
    for i in range(length, -1 ,-1 ):
        if decimal < 16 ** i:
            continue
        else:
            hexLength = i +1
            break
    print(hexLength)
    while decimal > 16 or hexLength > 1:
        temp = decimal // (16 ** (hexLength-1))
        #print(temp)
        char = decimalNumberToHexChar(temp)
        result += char
        decimal = decimal % (16 ** (hexLength-1))
        hexLength -= 1
    result += str(decimalNumberToHexChar(decimal))
    return result

def decimalNumberToHexChar(decimal):
    if decimal > 9:
        char = chr(ord("A") + (decimal-10))
    else:
        char = str(decimal)
    return char

if __name__ == '__main__':
    print(decimalToHex(16))
    

