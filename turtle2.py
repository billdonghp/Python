'''
半径：50 圆心60度的扇形
'''
import turtle

t = turtle.Pen()

t.goto(0, -50)

t.circle(50)  # 可以先画一个圆方便理解

t.circle(50,60)   # 第一个50为radius  第二个为60度圆心角

t.goto(0,0)   #返回原点
