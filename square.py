import turtle

def squares(t,order,size,x,y):
    if order > 0:
        squares(t,order-1,size/2,x-size/2,y+size/2)
        squares(t,order-1,size/2,x-size/2,y-size/2)
        squares(t,order-1,size/2,x+size/2,y-size/2)
        squares(t,order-1,size/2,x+size/2,y+size/2)
    else:
        t.up()
        t.setpos((x-size/2,y-size/2))
        t.down()
        t.begin_fill()
        t.setheading(0)
        for z in range(4):
            r=int(abs(x))
            if (r > 255) == True:
                r = 255%r
            g=int(abs(y))
            if (g > 255) == True:
                g = 255%g
            b=int(abs(x+y))
            if (b > 255) == True:
                b = 255%b
            t.fillcolor(0,0,0) #setting the fillcolor to 0,0,0 is awesome
            t.pencolor(g,r,b)
            t.forward(size)
            t.left(90)
        t.end_fill()
        
def squarefrac(t,order,size,x,y):
    t.hideturtle()
    t.tracer(100)
    t.colormode(255)
    for z in reversed(range(order)):
        squares(t,z,size,x,y)
    t.update()

squarefrac(turtle,8,450,0,0)
turtle.done()
