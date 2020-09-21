from turtle import *
from math import *
right(36)
color('red', 'red')


def star(a):
    for x in range(5):
        pd()
        fd(a)
        left(144)
        pu()


begin_fill()
star(30)
end_fill()
b = 30 * sin(radians(18)) / sin(radians(36))
c = 30 * sin(radians(18))
#h = (b ** 2 - c**2)**0.5
h = b * cos(radians(36))
for x in range(4):
    goto(sin(radians(54)) * 30 - c, sin(radians(36)) * 30 * -1 + h)
    #seth()
    left((4 - x) * 18)
    #pd()
    fd(30)
    right((4 - x) * 20)
    begin_fill()
    star(10)
    end_fill()
#goto(sin(radians(54)) * 30 -c,sin(radians(36)) * 30 *-1 + h)
ht()
