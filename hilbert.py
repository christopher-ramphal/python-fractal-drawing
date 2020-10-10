import turtle
def instructions(order,axiom='A'):
    rules=''
    final_axiom=''

    if (order == 0):
        return(axiom)
    else:
        for y in range(order):    
            for x in axiom:
                if x == 'A':
                    rules=rules + '-BF+AFA+FB-'
                elif x == 'B':
                    rules=rules + '+AF-BFB-FA+'
                else:
                    rules=rules+x
            axiom=rules
            rules=''
    for z in axiom:
        if z == 'A' or z=='B':
            final_axiom=final_axiom+''
        else:
            final_axiom=final_axiom+z
    return(final_axiom)

def hilcurv(t,order,size,x,y):
    t.hideturtle()
    t.up()
    t.setpos((x+size/2,y-size/2))
    t.down()
    t.tracer(5)    
    t.left(-180)
    t.colormode(255.0)
    rules=instructions(order)
    segments=rules.count('F')
    color_groups=(segments/255)/6
    counter=0
    r=0
    g=0
    b=0
    group_counter=0
    for step in rules:    
        if step == '+':
            t.left(90)
        elif step == '-':
            t.right(90)
        else:
            counter=counter+1
            if counter>color_groups:
                counter=0
                if group_counter == 0:
                    r=r+1
                    if r==255:
                        group_counter=group_counter+1
                if group_counter == 1:
                    g=g+1
                    if g==255:
                        group_counter=group_counter+1
                if group_counter == 2:
                    r=r-1
                    if r==0:
                        group_counter=group_counter+1
                if group_counter == 3:
                    b=b+1
                    if b==255:
                        group_counter=group_counter+1
                if group_counter == 4:
                    g=g-1
                    if g==0:
                        group_counter=group_counter+1
                if group_counter == 5:
                    r=r+1
            t.color(r,g,b)
            t.forward(size/2**order)
    t.update()
depth=int(input('Recursion Depth: '))
size=int(input('Size: '))
hilcurv(turtle,depth,size,0,0)
        

turtle.done()