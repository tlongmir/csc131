# Name:                 Katherine Crevisour
# Date:                 3/3/2021
# Program:              Assignment 1
# Description:          This program will draw some dice using the turtle graphics.

import random
import turtle

def main():

    # Window setup
    turtle.setup(1000, 900)
    win = turtle.Screen()
    win.bgcolor("lightBlue")
    
    ted = turtle.Turtle()
    ted.hideturtle()
    ted.speed(0)
    ted.fillcolor("white")
    

    #setting the coordinates of where the first dice will appear.
    x = -400
    y = 0
    width = 100
    
    #Drawing the white squares
    for dice in range(6):
        diceValue = dice + 1
        ted.begin_fill()
        ted.penup()
        if diceValue == 1:
                 ted.penup()
                 ted.goto(x + width//2, y + width//2)
                 ted.pendown()
                 ted.dot(10)
                 ted.penup()
        if diceValue == 2:
            ted.penup()
            ted.goto(x + width//4, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 20, y + width - 20)
            ted.pendown()
            ted.dot(10)
            ted.penup()
        if diceValue == 3:
            ted.penup()
            ted.goto(x + width//4, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width//2, y + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25 , y + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
        if diceValue == 4:
            ted.penup()
            ted.goto(x + width//4, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width//4, y + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25, y + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
        if diceValue == 5:
            ted.penup()
            ted.goto(x + width//4, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width//4, y + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25, y + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width//2, y + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
        if diceValue == 6:
            ted.penup()
            ted.goto(x + width//4, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width//4, y + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25, y + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25, y + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width - 25, y + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(x + width//4, y + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
        ted.begin_fill()
        ted.goto(x, y)
        ted.pendown()
        x = x + 150
        for squares in range(4):
           ted.forward(width)
           ted.left(90)
        ted.end_fill()

        
        
    a = -400
    b = -400
    ted.penup()
    ted.goto(a,b)
        
    for ranDice in range(2):
         randomValue = random.randint(1,6)
         ted.begin_fill()
         ted.penup()
         
         diceRoll = randomValue
    
    
         if diceRoll == 1 or diceRoll == 2 or diceRoll == 3 or diceRoll == 4 or diceRoll == 5 or diceRoll == 6 or diceRoll == 7:
             lessThan7 = diceRoll - 1
             prob = lessThan7/36 
         elif diceRoll == 7 or diceRoll == 8 or diceRoll == 9 or diceRoll == 10 or diceRoll == 11 or diceRoll == 12:
             moreThan13 = 13 - diceRoll
             prob = moreThan13/36

         print("The probability of rolling a", diceRoll, " is ", prob)
         if randomValue == 1:
            ted.penup()
            ted.goto(a + width//2, b + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
         if randomValue == 2:
            ted.penup()
            ted.goto(a + width//4, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 20, b + width - 20)
            ted.pendown()
            ted.dot(10)
            ted.penup()
         if randomValue == 3:
            ted.penup()
            ted.goto(a + width//4, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width//2, b + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25 , b + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
         if randomValue == 4:
            ted.penup()
            ted.goto(a + width//4, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width//4, b + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25, b + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
         if randomValue == 5:
            ted.penup()
            ted.goto(a + width//4, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width//4, b + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25, b + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width//2, b + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
         if randomValue == 6:
            ted.penup()
            ted.goto(a + width//4, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width//4, b + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25, b + width - 25)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25, b + width//4)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width - 25, b + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
            ted.goto(a + width//4, b + width//2)
            ted.pendown()
            ted.dot(10)
            ted.penup()
         ted.begin_fill()
         ted.goto(a, b)
         ted.pendown()
         a = a + 150
         for squares in range(4):
           ted.forward(width)
           ted.left(90)
         ted.end_fill()
    
   
    
    turtle.mainloop()
    
      
    
    




if __name__ == "__main__":
    main()
