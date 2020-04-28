def tur1():
    import turtle
    stop = eval(input("input stop\n"))
    color = ["RED","GREEN","YELLOW","BLUE"]
    #t = turtle.pen()
    for x in range(stop):
        turtle.pencolor(color[x%4])
        turtle.forward(x)
        turtle.left(91)

tur1()
