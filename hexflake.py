import turtle
from math import *

def hexagon (t,order,size,x,y):
    if order==0:
        t.up()
        t.setpos((x,y+size))
        t.down()
        t.setheading(0)
        t.begin_fill()
        for angle in [30,60,60,60,60,60]:
            r=int(abs(x))
            if (r > 255) == True:
                r = 255%r
            g=int(abs(y))
            if (g > 255) == True:
                g = 255%g
            b=int(abs(x+y))
            if (b > 255) == True:
                b = 255%b
            t.fillcolor(g,r,b) #setting the fillcolor to 0,0,0 is awesome
            t.pencolor(g,r,b)
            t.right(angle)
            t.forward(size)
        t.end_fill()
        
    else:
        hexagon(t,order-1,size/3,x,y)
        hexagon(t,order-1,size/3,x,y+2*size/3)
        hexagon(t,order-1,size/3,x+size*2*cos(pi/6)/3,y+size/3)
        hexagon(t,order-1,size/3,x+size*2*cos(pi/6)/3,y-size/3)
        hexagon(t,order-1,size/3,x,y-2*size/3)
        hexagon(t,order-1,size/3,x-size*2*cos(pi/6)/3,y-size/3)
        hexagon(t,order-1,size/3,x-size*2*cos(pi/6)/3,y+size/3)

def hexfrac(t,order,size,x,y):
    t.hideturtle()
    t.tracer(100)
    t.colormode(255)
    hexagon(t,order,size,x,y)
    t.update()
    
hexfrac(turtle,5,400,0,0)
turtle.done()