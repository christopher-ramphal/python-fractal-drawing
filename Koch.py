import turtle
def Koch(t,order,size):
    if order == 0:
        x,y=t.pos()
        r=int(abs(x))
        if (r > 255) == True:
            r = 255%r
        g=int(abs(y))
        if (g > 255) == True:
            g = 255%g
        b=int(abs(x+y))
        if (b > 255) == True:
            b = 255%b
        t.pencolor(r,g,b)
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           Koch(t, order-1, size/3)
           t.left(angle)

def Snowflake(t,order,size):
    t.hideturtle()
    t.up()
    startx=-size/2
    starty=-size/3**.5
    t.setposition((startx,starty/2))
    t.down()
    t.tracer(100)
    t.colormode(255)
    for angle in [60,-120,-120]:
        t.left(angle)
        Koch(t,order,size)
    t.update()
Snowflake(turtle,6,500)
turtle.done()
