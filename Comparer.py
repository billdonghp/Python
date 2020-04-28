''' 备胎选择器 加分项：有爱、帅气、勇敢、勤劳、有钱

'''

nameList = [
    "穷，勤劳、勇敢、有爱、帅气张三",
    "有钱，懒、勇敢、有爱、丑李四",
    "穷，懒、懦弱、自私、帅气王五",
    "有钱，懒、懦弱、自私、帅气赵六",
    "穷，勤劳、勇敢、有爱、帅气付七",

    ]

max = -1

theMan = None

for i in range(len(nameList)):
    temp = nameList[i]
    score = 0
    if temp.find("有钱") < 0:
        print("【%s】因为没有钱，直接出局"%(temp))
        continue
    else:
        score += 1
    if temp.find("有爱") >=0:
        score += 1
    if temp.find("帅气") >=0:
        score += 1
    if temp.find("勇敢") >=0:
        score += 1
    if temp.find("勤劳") >=0:
        score += 1
    #print("【%s】综合得分：%d!"%(temp,score))
    if score > max:
        max = score
        theMan = temp

print("【%s】已转正，得分：%d!"%(theMan,max))
