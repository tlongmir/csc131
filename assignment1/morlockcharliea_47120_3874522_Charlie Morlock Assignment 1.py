#Charlie Morlock
#03/04/2021
#Assignment 1
#This program draws 6 dice valued from 1-6, and then draws 2 more dice at random
#values. The program then computes the probability that you will roll the sum
#of the two dice. 

import turtle
import random

def main():

    turtle.setup(800, 300)
    win = turtle.Screen()
    win.bgcolor("blue")

    
    width = 50
    radius = width//6
    bob = turtle.Turtle()

    x = -250
    y = 100
    dice = 6
    dieValue = 0

    p1 = width*(1/4)
    p2 = width*(1/2)
    p3 = width*(3/4)

    #Draws first 6 dice.
    for d in range(dice):
        dieValue = d
        bob.color("white")
        bob.penup()
        bob.goto(x,y)
        bob.pendown()
        bob.begin_fill()
        for p in range(4):
            bob.forward(width)
            bob.right(90)
        bob.end_fill()
        bob.penup()
        if dieValue == 0:
            bob.goto(x+p2, y-p2)
            bob.dot(radius, "black")
        elif dieValue == 1:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
        elif dieValue == 2:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p2, y-p2)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
        elif dieValue == 3:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p3)
            bob.dot(radius, "black")
        elif dieValue == 4:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p2, y-p2)
            bob.dot(radius, "black")
        else:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p2)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p2)
            bob.dot(radius, "black")
        x += 1.5*width

    x = -50
    y = -75
    
    #Draws 2 random dice
    for z in range(2):
        dieValue = random.randint(1,6)
        #Stores value of both dice
        if z == 0:
            die1 = dieValue
        elif z == 1:
            die2 = dieValue
        bob.color("white")
        bob.penup()
        bob.goto(x,y)
        bob.pendown()
        bob.begin_fill()
        for b in range(4):
            bob.forward(width)
            bob.right(90)
        bob.end_fill()
        bob.penup()
        if dieValue == 1:
            bob.goto(x+p2, y-p2)
            bob.dot(radius, "black")
        elif dieValue == 2:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
        elif dieValue == 3:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p2, y-p2)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
        elif dieValue == 4:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p3)
            bob.dot(radius, "black")
        elif dieValue == 5:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p2, y-p2)
            bob.dot(radius, "black")
        else:
            bob.goto(x+p1, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p1)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p2)
            bob.dot(radius, "black")
            bob.goto(x+p3, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p3)
            bob.dot(radius, "black")
            bob.goto(x+p1, y-p2)
            bob.dot(radius, "black")
        x += 1.5*width

    total = die1+die2

    #Calculates probability of rolling sum of dice
    if total <= 7:
        chance = total - 1
        prob = (chance/36)*100
    else:
        chance = 13 - total
        prob = (chance/36)*100

    print("The probability of rolling a " + format(total, "d") + " is: " + format(prob, ".4f")+"%")
        
                
if __name__ == "__main__":
    main()
    
