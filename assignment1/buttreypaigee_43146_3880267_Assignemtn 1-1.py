#Name: P.Buttrey
#Date: 03/042/2021
#Description: creating dice 

import turtle
import math
import random

def main():
    turtle.setup(800,800)
    win = turtle.Screen()
    win.bgcolor("green")
    pop = turtle.Turtle()
    pop.speed(0)
    x = -300
    y = -100
    width = 75
    size = width//6
    for Dice in range (6):
        dieValue = Dice + 1
        pop.penup()
        pop.goto(x,y)
        pop.pendown()
        pop.pencolor("black")
        pop.fillcolor("white")
        pop.begin_fill()
        for Square in range (4):
            pop.forward(width)
            pop.right(90)
        pop.end_fill()
        pop.penup()
        if dieValue == 1:
            pop.goto(x + width //2, y - width //2)
            pop.dot(size)
        elif dieValue == 2:
            pop.goto(x + width//4, y - width//4)
            pop.dot(size)
            pop.goto(x + (3 * width // 4), y - (3 * width // 4))
            pop.dot(size)
        elif dieValue == 3:
            pop.goto(x + width // 2, y - width //2)
            pop.dot(size)
            pop.goto(x + width//4, y - width//4)
            pop.dot(size)
            pop.goto(x + (3 * width // 4), y - (3 * width // 4))
            pop.dot(size)
        elif dieValue == 4:
            pop.goto(x + width//4, y - width//4)
            pop.dot(size)
            pop.goto(x + (3 * width // 4), y - (3 * width // 4))
            pop.dot(size)
            pop.goto(x + width // 4, y - (3 * width // 4))
            pop.dot(size)
            pop.goto(x + (3 * width //4), y - width // 4)
            pop.dot(size)
        elif dieValue == 5:
            pop.goto(x + width //2, y - width //2)
            pop.dot(size)
            pop.goto(x + width//4, y - width//4)
            pop.dot(size)
            pop.goto(x + (3 * width // 4), y - (3 * width // 4))
            pop.dot(size)
            pop.goto(x + width // 4, y - (3 * width // 4))
            pop.dot(size)
            pop.goto(x + (3 * width //4), y - width // 4)
            pop.dot(size)
        else: 
            pop.goto(x + width//4, y - width//4)
            pop.dot(size)
            pop.goto(x + (3 * width // 4), y - (3 * width // 4))
            pop.dot(size)
            pop.goto(x + width // 4, y - (3 * width // 4))
            pop.dot(size)
            pop.goto(x + (3 * width //4), y - width // 4)
            pop.dot(size)
            pop.goto(x + width //4, y - width // 2)
            pop.dot(size)
            pop.goto(x + (3* width//4), y - width //2)
            pop.dot(size)
        
        x += 1.5 * width
def paige():
        pop = turtle.Turtle()
        pop.speed(0)
        x = -300
        y = -300
        width = 75
        size = width//6
        Summation = 0
        for Dice in range (2):
            dieValue = random.randint(1,6)
            Summation += dieValue
            Probability = (Summation - 1) /36
            pop.penup()
            pop.goto(x,y)
            pop.pendown()
            pop.pencolor("black")
            pop.fillcolor("white")
            pop.begin_fill()
            for Square in range (4):
                pop.forward(width)
                pop.right(90)
            pop.end_fill()
            pop.penup()
            if dieValue == 1:
                pop.goto(x + width //2, y - width //2)
                pop.dot(size)
            elif dieValue == 2:
                pop.goto(x + width//4, y - width//4)
                pop.dot(size)
                pop.goto(x + (3 * width // 4), y - (3 * width // 4))
                pop.dot(size)
            elif dieValue == 3:
                pop.goto(x + width // 2, y - width //2)
                pop.dot(size)
                pop.goto(x + width//4, y - width//4)
                pop.dot(size)
                pop.goto(x + (3 * width // 4), y - (3 * width // 4))
                pop.dot(size)
            elif dieValue == 4:
                pop.goto(x + width//4, y - width//4)
                pop.dot(size)
                pop.goto(x + (3 * width // 4), y - (3 * width // 4))
                pop.dot(size)
                pop.goto(x + width // 4, y - (3 * width // 4))
                pop.dot(size)
                pop.goto(x + (3 * width //4), y - width // 4)
                pop.dot(size)
            elif dieValue == 5:
                pop.goto(x + width //2, y - width //2)
                pop.dot(size)
                pop.goto(x + width//4, y - width//4)
                pop.dot(size)
                pop.goto(x + (3 * width // 4), y - (3 * width // 4))
                pop.dot(size)
                pop.goto(x + width // 4, y - (3 * width // 4))
                pop.dot(size)
                pop.goto(x + (3 * width //4), y - width // 4)
                pop.dot(size)
            else: 
                pop.goto(x + width//4, y - width//4)
                pop.dot(size)
                pop.goto(x + (3 * width // 4), y - (3 * width // 4))
                pop.dot(size)
                pop.goto(x + width // 4, y - (3 * width // 4))
                pop.dot(size)
                pop.goto(x + (3 * width //4), y - width // 4)
                pop.dot(size)
                pop.goto(x + width //4, y - width // 2)
                pop.dot(size)
                pop.goto(x + (3* width//4), y - width //2)
                pop.dot(size)
            
            x += 1.5 * width
        print("The probability of rolling a", Summation, "is", format(Probability,".4%"))
     
        
        
        
        
    
        

if __name__=="__main__":
    main()
    paige()
        
    
