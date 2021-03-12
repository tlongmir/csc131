#Name: Eduardo Garcia-Lopez
#Date: 03/04/21
#Description:Will draw 6 dice in order and then will draw 2 random dice above and will calcuate the probability of rolling the sum of those 2 dice.
import turtle
import random
def main():
    
    turtle.setup(600,300,0,0)
    win = turtle.Screen()
    win.bgcolor("Red")

    width=50 #width of dice
    x=-200#position of first dice
    y=0#position of first dice
    dievalue=0
    dievalue2=random.randint(1,6)
    dievalue3=random.randint(1,6)
    dievalue4=dievalue2+dievalue3
    dotwidth=1/6*width
    if dievalue3+dievalue2 <= 7:#this will figure out probability of rolling the 2 random dice
        probability=(dievalue4-1)/36*100
    else:
        probability=(13-dievalue4)/36*100

    

    print("The probability of rolling a",dievalue4,"is",probability,"%")
    
    ant=turtle.Turtle()#Dice
    jo=turtle.Turtle()#Dots
    jo.speed(0)
    ant.speed(0)
    jo.hideturtle()
    jo.fillcolor("Black")
    ant.fillcolor("White")
    for i in range (6):
        ant.penup()
        ant.goto(x,y)
        ant.pendown()
        ant.begin_fill()
        dievalue=dievalue+1
        for j in range (4):#Dice loop that will make square
            ant.fd(width)
            ant.rt(90)
        ant.end_fill()
        jo.penup()
        if dievalue == 1:#these if and else statements will be what make the dots on the squares
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
        elif dievalue == 2:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue == 3:
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue == 4:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue == 5:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
        else:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-1/2*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/2*width)
            jo.dot(dotwidth)
        x=x+1.5*width

    x=-200
    y=100
    for i in range (1):#this for loop will create the first random die
        ant.penup()
        ant.goto(x,y)
        ant.pendown()
        ant.begin_fill()
        for j in range (4):
            ant.fd(width)
            ant.rt(90)
        ant.end_fill()
        jo.penup()
        if dievalue2 == 1:
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
        elif dievalue2 == 2:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue2 == 3:
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue2 == 4:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue2 == 5:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
        else:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-1/2*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/2*width)
            jo.dot(dotwidth)
        x=x+1.5*width

    for i in range (1):#this loop will create the second random die
        ant.penup()
        ant.goto(x,y)
        ant.pendown()
        ant.begin_fill()
        for j in range (4):
            ant.fd(width)
            ant.rt(90)
        ant.end_fill()
        jo.penup()
        if dievalue3 == 1:
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
        elif dievalue3 == 2:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue3 == 3:
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue3 == 4:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
        elif dievalue3 == 5:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/2*width,y-1/2*width)
            jo.dot(dotwidth)
        else:
            jo.goto(x+1/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/4*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-3/4*width)
            jo.dot(dotwidth)
            jo.goto(x+1/4*width,y-1/2*width)
            jo.dot(dotwidth)
            jo.goto(x+3/4*width,y-1/2*width)
            jo.dot(dotwidth)
        x=x+1.5*width


    turtle.mainloop()

if __name__ == "__main__":
    main()
