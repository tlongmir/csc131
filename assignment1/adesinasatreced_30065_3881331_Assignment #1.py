# Name: Satrece Adesina
# Date: 3/2/2021
# Program Name: Assignment #1
# Description: This program will draw dice so that we can soon this into a game in a later assignment.

import turtle
import random

S = turtle.Turtle()
DiceValue = random.randint(1,6)
Width = 175
Location = 1.5 * Width
SizeDots = Width // 6

def main():
    turtle.setup(200,200)
    win = turtle.Screen()
    win.bgcolor("lavender")

    for i in range(1):
        S.penup()
        S.setpos(-650,150)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()
        S.penup()
        S.setpos(-565,240)
        S.pendown()
        S.dot(29, "black")

        S.penup()
        S.goto(-450,150)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()
        S.penup()
        S.setpos(-305, 190)
        S.dot(29, "black")
        S.penup()
        S.setpos(-415,285)
        S.pendown()
        S.dot(29, "black")

        S.penup()
        S.goto(-250,150)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()
        S.penup()
        S.setpos(-220, 190)
        S.dot(29, "black")
        S.penup()
        S.setpos(-165, 240)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(-115, 290)
        S.dot(29, "black")

        S.penup()
        S.goto(-50,150)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()
        S.penup()
        S.setpos(-10, 185)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(95, 185)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(95, 295)
        S.dot(29, "black")
        S.penup()
        S.setpos(-10, 295)
        S.pendown()
        S.dot(29, "black")

        S.penup()
        S.goto(150,150)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()
        S.penup()
        S.setpos(300, 185)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(185, 185)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(235, 240)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(185, 300)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(275, 300)
        S.pendown()
        S.dot(29, "black")

        S.penup()
        S.goto(350,150)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()
        S.penup()
        S.setpos(475, 200)
        S.dot(29, "black")
        S.penup()
        S.setpos(385, 200)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(385, 250)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(385, 300)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(475, 250)
        S.pendown()
        S.dot(29, "black")
        S.penup()
        S.setpos(475, 300)
        S.pendown()
        S.dot(29, "black")

        S.penup()
        S.goto(-250,-300)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()

        S.penup()
        S.goto(-50, -300)
        S.pendown()
        S.fillcolor("white")
        S.begin_fill()
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.fd(175)
        S.lt(90)
        S.end_fill()

        # Fix Dots placements
        # Figure out variables

        S.hideturtle()
if __name__ == "__main__":
    main()
