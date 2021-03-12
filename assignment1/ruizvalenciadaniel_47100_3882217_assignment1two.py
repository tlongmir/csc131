# Name: Daniel Ruiz Valencia
# Date: 3/2/2021
# Program Name: Dice Test
# Description: This program will draw some dice, randomize two numbers on two different dice, and calculate the probability of the numbers you rolled on the two dice. 

import turtle
import random

def main():
    turtle.setup(900,500)
    win = turtle.Screen()
    win.bgcolor('HotPink')

    dan=turtle.Turtle()

    dicevalue = 1
    x = -575
    y = 200
    width = 100
    dotsize = width // 6

    for a in range(6):
        # How to draw multiple squares.
        dan.penup()
        x += 1.5 * width
        dan.goto(x,y)
        dan.pendown()
        dan.begin_fill()
        for b in range(4):
            # How to draw the actual squares.
            dan.fillcolor('white')
            dan.pendown()
            dan.forward(width)
            dan.right(90)
            dan.end_fill()
            b += 1

        dan.begin_fill()
        dan.fillcolor('black')
        dan.begin_fill()
        dan.penup()

            # How to draw the dots on the die.

        if dicevalue == 1:
            dan.goto(x+.75*width,y-.25*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
        elif dicevalue == 2:
            dan.goto(x+.75*width,y-.25*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
            dan.penup()
            dan.goto(x+.25*width,y-.75*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
        elif dicevalue == 3:
            dan.goto(x+.75*width,y-.25*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
            dan.penup()
            dan.goto(x+.25*width,y-.75*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
        elif dicevalue == 4:
            dan.goto(x+.75*width,y-.25*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
            dan.penup()
            dan.goto(x+.25*width,y-.75*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
        elif dicevalue == 5:
            dan.goto(x+.75*width,y-.25*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
            dan.penup()
            dan.goto(x+.25*width,y-.75*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
        elif dicevalue == 6:
            dan.goto(x+.75*width,y-.25*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
            dan.penup()
            dan.goto(x+.25*width,y-.75*width)
            dan.pendown()
            dan.begin_fill()
            dan.dot(dotsize)
            dan.end_fill()
        dan.end_fill( 
  
    
if __name__ == "__main__":
    main()
