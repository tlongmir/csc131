#Ethan Bevenour
#3/2/2021
#In this assignment, you will draw some dice.  This will not be a game yet, but we will make it into a game later.
#Right now, you should be able to draws some dice looking shapes on the screen.

import turtle
import random

def main():
    turtle.setup(900, 900)
    win = turtle.Screen()
    win.bgcolor('MediumAquamarine')
    Larry = turtle.Turtle()
    Width = 70
    x = -300
    y = 300
    Larry.speed(0)
    Dotsize = Width // 7
    Larry.fillcolor('white')
    for i in range(6):
        Dievalue = i + 1
        Larry.penup()
        Larry.goto(x, y)
        Larry.pendown()
        Larry.begin_fill()
        for _ in range(4):
            Larry.forward(Width)
            Larry.right(90)
        Larry.end_fill()
        Larry.penup()
        if Dievalue == 1:
            Larry.goto(x + 2/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 2:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 3:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 2/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 4:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 5:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 2/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        else:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        x = x + Width * 1.5



    #Part 2
    x = 0 - Width * 1.5
    y = 0 + Width * 1.5
    Dievalue2 = 0
    for i in range(2):
        Dievalue = random.randint(1, 6)
        Dievalue2 = Dievalue2 + Dievalue
        Larry.goto(x, y)
        Larry.pendown()
        Larry.begin_fill()
        for _ in range(4):
            Larry.forward(Width)
            Larry.right(90)
        Larry.end_fill()
        Larry.penup()
        if Dievalue == 1:
            Larry.goto(x + 2/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 2:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 3:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 2/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 4:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
        elif Dievalue == 5:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 2/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        else:
            Larry.goto(x + 3/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 1/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 3/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 3/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
            Larry.goto(x + 1/4 * Width, y - 2/4 * Width)
            Larry.dot(Dotsize)
        x = x + Width * 1.5



    #Part 3
    NumOFrolls = 0
    if Dievalue2 <= 7:
        NumOFrolls = Dievalue2 - 1
    else:
        NumOFrolls = 13 - Dievalue2
    Probability = (NumOFrolls / 36) * 100
    print('The probability of rolling a ' +str(Dievalue2) + ' is ' + str(format(Probability, "2.4f")) + '%')
    
    



        
    turtle.mainloop()

if __name__ == "__main__":
    main()
