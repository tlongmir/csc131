#Name: Zachary Canter
#Date: 03/02/2021
#Description: This program will draw dice and calculate probability of roll

import turtle
import random

turtle.speed(0)
turtle.setup(1000,800)


Rachel = turtle.Turtle()
random.randint(0,6)
width = 140
        
def draw(num, x, y):
    # Draw dice outline at position x,y
    Rachel.penup()
    Rachel.goto(x, y)
    Rachel.pendown()
    Rachel.fillcolor("white")
    Rachel.begin_fill()
    Rachel.forward(140)
    Rachel.left(90)
    Rachel.forward(140)
    Rachel.left(90)
    Rachel.forward(140)
    Rachel.left(90)
    Rachel.forward(140)
    Rachel.left(90)
    Rachel.end_fill()
    Rachel.penup()

    if num == 1:
        # Draw dice pips for a 1 roll    
        Rachel.goto( x + ( width / 2 ), y + ( width / 2 ) )
        Rachel.dot(width // 6, "black")

    if num == 2:
        # Draw dice pips a 2 roll
        Rachel.setpos( x + ( width / 4 ), y + ( width / 4 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width  * .75 ), y + ( width * .75 ) )
        Rachel.pendown()
        Rachel.dot(width // 6, "black")
        
    if num == 3:
        # Draw dice pips a 3 roll
        Rachel.setpos( x + ( width / 4 ), y + ( width / 4 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width / 2 ), y + ( width / 2 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width  * .75 ), y + ( width * .75 ) )
        Rachel.pendown()
        Rachel.dot(width // 6, "black")
        
    if num == 4:
        # Draw dice pips a 4 roll
        Rachel.setpos( x + ( width * .25 ), y + ( width * .25 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .25 ), y + ( width * .75 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .75 ), y + ( width * .25 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .75 ), y + ( width * .75 ) )
        Rachel.dot(width // 6, "black")
        Rachel.pendown()
        Rachel.dot(width // 6, "black")
        
    if num == 5:
        # Draw dice pips a 5 roll
        Rachel.setpos( x + ( width * .25 ), y + ( width * .25 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .25 ), y + ( width * .75 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .75 ), y + ( width * .25 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .75 ), y + ( width * .75 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width / 2 ), y + ( width / 2 ) )
        Rachel.pendown()
        Rachel.dot(width // 6, "black")
        
    if num == 6:
        # Draw dice pips a 6 roll
        Rachel.setpos( x + ( width * .25 ), y + ( width * .25 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .25 ), y + ( width * .75 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .75 ), y + ( width * .25 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .75 ), y + ( width * .75 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width / 4 ), y + ( width / 2 ) )
        Rachel.dot(width // 6, "black")
        Rachel.penup()
        Rachel.setpos( x + ( width * .75  ), y + ( width / 2 ) )
        Rachel.pendown()
        Rachel.dot(width // 6, "black")

def main():
    win = turtle.Screen()
    win.setup(width=1000,height=800)
    win.bgcolor("LightPink")
    Rachel.hideturtle()

    x = -650
    y = 150

    for i in range(1,7):
        draw(i,x,y)
        x+=200
    same = 0
    totalRolls = 1000

num1 = random.randint(1,6)
draw(num1,-250,-300)
num2 = random.randint(1,6)
draw(num2,-50,-300)

value = num1 + num2
if value<= 7:
    prob = ((value - 1) * 100) / 36
else:
    prob = ((13 - value) * 100) / 36

print('probability:', prob)
if __name__ == "__main__":
    main()

    






