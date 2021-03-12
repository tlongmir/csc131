# Name: Jonah Gloss
# Date: 03/4/2021
# Description: This program creates 8 dice. The first 6 dice display values
# 1-6, the other 2 dice display random generated values. The last 2 dice
# then calculate the probability of rolling the sum of the 2 values.

import turtle
import random

def main():
    #Turtle Setup
    dice = turtle.Turtle()

    turtle.setup(800, 600)
    win = turtle.Screen()
    win.bgcolor("PeachPuff")

    width = 100

    dice.speed(0)

    dice.penup()

    #DICE PLACEMENT

    # DICE 1
    dice.goto(-425,0)
    dice.pendown()
    dice.fillcolor("white")
    dice.begin_fill()

    for a in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.fillcolor("White")

    dice.penup()

    #DICE 2
    dice.goto(-275, 0)
    dice.pendown()

    dice.begin_fill()

    for b in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.penup()

    #DICE 3
    dice.goto(-125, 0)
    dice.pendown()

    dice.begin_fill()

    for c in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.penup()

    #DICE 4
    dice.goto(25, 0)
    dice.pendown()

    dice.begin_fill()

    for d in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.penup()

    #DICE 5
    dice.goto(175, 0)
    dice.pendown()

    dice.begin_fill()

    for e in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.penup()

    #DICE 6
    dice.goto(325, 0)
    dice.pendown()

    dice.begin_fill()

    for f in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.penup()

    dice.goto(-425,0)

    #Dot Setup for dice 1-6
    for g in range(6):
        dieValue = g + 1

        if dieValue == 1:
            dice.goto(-375,-50)
            dice.dot(width // 6)

        elif dieValue == 2:
            dice.goto(-200, -25)
            dice.dot(width // 6)
            dice.goto(-250, -75)
            dice.dot(width // 6)

        elif dieValue == 3:
            dice.goto(-50,-25)
            dice.dot(width // 6)
            dice.goto(-75,-50)
            dice.dot(width // 6)
            dice.goto(-100,-75)
            dice.dot(width // 6)

        elif dieValue == 4:
            dice.goto(50,-25)
            dice.dot(width // 6)
            dice.goto(100,-25)
            dice.dot(width // 6)
            dice.goto(100,-75)
            dice.dot(width // 6)
            dice.goto(50, -75)
            dice.dot(width // 6)

        elif dieValue == 5:
            dice.goto(200,-25)
            dice.dot(width // 6)
            dice.goto(200,-75)
            dice.dot(width // 6)
            dice.goto(250,-25)
            dice.dot(width // 6)
            dice.goto(250,-75)
            dice.dot(width // 6)
            dice.goto(225,-50)
            dice.dot(width // 6)

        else:
            dice.goto(350,-25)
            dice.dot(width // 6)
            dice.goto(350,-50)
            dice.dot(width // 6)
            dice.goto(350,-75)
            dice.dot(width // 6)
            dice.goto(400,-25)
            dice.dot(width // 6)
            dice.goto(400,-50)
            dice.dot(width // 6)
            dice.goto(400,-75)
            dice.dot(width // 6)

    #DICE 7-8 Placement

    dice.goto(-125, -200)
    dice.pendown()

    dice.begin_fill()

    #DICE 7
    for c in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.penup()


    dice.goto(25, -200)
    dice.pendown()

    dice.begin_fill()

    #DICE 8
    for d in range(4):
        dice.forward(width)
        dice.right(90)

    dice.end_fill()

    dice.penup()

    #Random dot Setup for dice 7-8
    dieValue = random.randint(1,6)

    if dieValue == 1:
        dice.goto(75,-250)
        dice.dot(width // 6)

    elif dieValue == 2:
        dice.goto(100, -225)
        dice.dot(width // 6)
        dice.goto(50, -275)
        dice.dot(width // 6)

    elif dieValue == 3:
        dice.goto(100,-225)
        dice.dot(width // 6)
        dice.goto(75,-250)
        dice.dot(width // 6)
        dice.goto(50,-275)
        dice.dot(width // 6)

    elif dieValue == 4:
        dice.goto(100,-225)
        dice.dot(width // 6)
        dice.goto(100,-275)
        dice.dot(width // 6)
        dice.goto(50,-275)
        dice.dot(width // 6)
        dice.goto(50, -225)
        dice.dot(width // 6)

    elif dieValue == 5:
        dice.goto(100,-225)
        dice.dot(width // 6)
        dice.goto(100,-275)
        dice.dot(width // 6)
        dice.goto(50,-275)
        dice.dot(width // 6)
        dice.goto(50,-225)
        dice.dot(width // 6)
        dice.goto(75,-250)
        dice.dot(width // 6)

    else:
        dice.goto(50,-225)
        dice.dot(width // 6)
        dice.goto(50,-250)
        dice.dot(width // 6)
        dice.goto(50,-275)
        dice.dot(width // 6)
        dice.goto(100,-225)
        dice.dot(width // 6)
        dice.goto(100,-250)
        dice.dot(width // 6)
        dice.goto(100,-275)
        dice.dot(width // 6)

    dieValue2 = random.randint(1, 6)

    if dieValue2 == 1:
        dice.goto(-75, -250)
        dice.dot(width // 6)

    elif dieValue2 == 2:
        dice.goto(-100, -225)
        dice.dot(width // 6)
        dice.goto(-50, -275)
        dice.dot(width // 6)

    elif dieValue2 == 3:
        dice.goto(-100, -225)
        dice.dot(width // 6)
        dice.goto(-75, -250)
        dice.dot(width // 6)
        dice.goto(-50, -275)
        dice.dot(width // 6)

    elif dieValue2 == 4:
        dice.goto(-100, -225)
        dice.dot(width // 6)
        dice.goto(-100, -275)
        dice.dot(width // 6)
        dice.goto(-50, -275)
        dice.dot(width // 6)
        dice.goto(-50, -225)
        dice.dot(width // 6)

    elif dieValue2 == 5:
        dice.goto(-100, -225)
        dice.dot(width // 6)
        dice.goto(-100, -275)
        dice.dot(width // 6)
        dice.goto(-50, -275)
        dice.dot(width // 6)
        dice.goto(-50, -225)
        dice.dot(width // 6)
        dice.goto(-75, -250)
        dice.dot(width // 6)

    else:
        dice.goto(-50, -225)
        dice.dot(width // 6)
        dice.goto(-50, -250)
        dice.dot(width // 6)
        dice.goto(-50, -275)
        dice.dot(width // 6)
        dice.goto(-100, -225)
        dice.dot(width // 6)
        dice.goto(-100, -250)
        dice.dot(width // 6)
        dice.goto(-100, -275)
        dice.dot(width // 6)

    x = dieValue + dieValue2

    #Probability Calculation if Statements
    if x <= 7:
        prob = x - 1
        prob = (prob / 36) * 10**2
        probsimp = format(prob, "0.4f")
        print("The probability of rolling a", x, "is", probsimp)
    else:
        prob = 13 - x
        prob = (prob / 36) * 10**2
        probsimp = format(prob, "0.4f")
        print("The probability of rolling a", x, "is", probsimp)


    turtle.mainloop()

if __name__ == "__main__":
    main()