import turtle
from math import *

def triangle(t,order,size,x,y):
    if order==0:
        t.up()
        t.setpos(x-size/2,y+size/(2*3**.5))
        t.down()
        t.setheading(0)
        t.begin_fill()
        for angle in [60,-120,-120,60,120,120]:
            r=int(abs(x))
            if (r > 255) == True:
                r = 255%r
            g=int(abs(y))
            if (g > 255) == True:
                g = 255%g
            b=int(abs(x+y))
            if (b > 255) == True:
                b = 255%b
            t.fillcolor(g,r,b)
            t.pencolor(g,r,b)
            t.left(angle)
            t.forward(size)
        t.end_fill()
        t.up()
        tp=t.pos()
        t.setpos((tp[0]+size,tp[1]))
        t.down()
        t.begin_fill()
        for angle in [180,120,120]:    
            r=int(abs(x))
            if (r > 255) == True:
                r = 255%r
            g=int(abs(y))
            if (g > 255) == True:
                g = 255%g
            b=int(abs(x+y))
            if (b > 255) == True:
                b = 255%b
            t.fillcolor(g,r,b)
            t.pencolor(g,r,b)
            t.right(angle)
            t.forward(size)
        t.end_fill()
    else:
        triangle(t,order-1,size/2,x,y+size/(3**.5))
        triangle(t,order-1,size/2,x+size/(2),y-size/(2*3**.5))
        triangle(t,order-1,size/2,x-size/(2),y-size/(2*3**.5))

def siertype1(t,order,size,x,y):
    triangle(t,order,size,x,y)

def upsidedown(t,order,size,x,y): 
    if order==0:
        t.setheading(0)
        t.up()
        t.setpos(x-size/2,y+size/(2*3**.5))
        t.down()
        t.begin_fill()
        for angle in [120,120,0]:
            t.forward(size)
            t.right(angle)
        t.end_fill()
    else:
        upsidedown(t,order-1,size/2,x,y+size/(3**.5))
        upsidedown(t,order-1,size/2,x+size/2,y-size/(2*3**.5))
        upsidedown(t,order-1,size/2,x-size/2,y-size/(2*3**.5))

def siertype2(t,order,size,x,y,col):  
    for z in range(order):
        t.fillcolor(col)
        t.pencolor(col)
        upsidedown(t,z,size,x,y)

def siertriangle(t,order,size,x,y,col,fill):
    t.hideturtle()
    t.tracer(100)
    t.colormode(255)
    if order==0:
        t.fillcolor(col)
        t.pencolor(col)
        t.up()
        t.setpos(x-2*size/2,y-2*size/(2*3**.5))
        t.setheading(0)
        t.down()
        t.begin_fill()
        for angle in [-60,120,120]:    
            t.right(angle)
            t.forward(2*size)
        t.end_fill()
    else:
        if fill == True:
            siertype2(t,order,size,x,y,col)
        siertype1(t,order-1,size,x,y)
    t.update()

siertriangle(turtle,7,200,0,0,(0,0,0),False)

turtle.done()