import random

def getRandomCharBetween(startChar,endChar):
    start = ord(startChar)
    end = ord(endChar)
    index = random.randint(start,end)
    char = chr(index)
    return char

def getRandomLowerCase():
    letter = getRandomCharBetween('a','z')
    return letter


def getRandomUpperCase():
    letter = getRandomCharBetween('A','Z')
    return letter

def getRandomNumber():
    letter = getRandomCharBetween('0','9')
    return letter
def getRandomAscii():
    startChar = chr(0)
    endChar = chr(127)
    letter = getRandomCharBetween(startChar,endChar)
    return letter

if __name__ == '__main__':
    for x in range(100):
        #print(getRandomLowerCase())
        #print(getRandomUpperCase())
        #print(getRandomAscii())
        print(getRandomNumber())
