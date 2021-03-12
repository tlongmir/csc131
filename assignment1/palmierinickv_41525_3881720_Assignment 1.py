# Name: Nick Palmieri
# Date: 02/05/2021
# Description: Drawing Dice


''' This program will be able to draw 8 different dice
and tell you the probability of each dice being landed on'''

def main():

    import turtle
    import random

    turtle.setup(1000,1000)
    win = turtle.Screen()
    win.bgcolor("blue")
    width = 60
    x = -450
    y = 300
    sizeofdot =  width // 6
    lego = turtle.Turtle()
    lego.penup()
    lego.goto(x,y)
    lego.pendown()
    lego.fillcolor("white")
    lego.begin_fill()
    for a in [1, 2, 3, 4, 5, 6]:
            dievalue = a
            lego.goto(x,y)
            lego.pendown()
            lego.fillcolor("white")
            lego.begin_fill()
            for b in range(4):
                lego.forward(width)
                lego.right(90)
            lego.end_fill()
            lego.penup()
            if dievalue == 1:
                lego.goto(x + .5 * width, y - .5 * width)
                lego.dot(sizeofdot)

            elif dievalue == 2:
                lego.goto(x + .75 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .75 * width)
                lego.dot(sizeofdot)
        
            elif dievalue == 3:
                lego.goto(x + .75 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .75 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .5 * width, y - .5 * width)
                lego.dot(sizeofdot)

            elif dievalue == 4:
                lego.goto(x + .75 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .75 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .75 * width, y - .75 * width)
                lego.dot(sizeofdot)

            elif dievalue == 5:
                lego.goto(x + .75 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .75 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .75 * width, y - .75 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .5 * width, y - .5 * width)
                lego.dot(sizeofdot)
            
            
            else:
                lego.goto(x + .75 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .75 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .25 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .75 * width, y - .75 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .25 * width, y - .50 * width)
                lego.dot(sizeofdot)
                lego.goto(x + .75 * width, y - .50 * width)
                lego.dot(sizeofdot)
            
    
                    
    
            
                
            
            x = x + 1.5 * width
#Part 2
    for c in [7, 8]:
        dievalue = c
        lego.goto(x * 1.5, y * .5)
        lego.pendown()
        lego.fillcolor("white")
        lego.begin_fill()
        for d in range(4):
            lego.forward(width)
            lego.right(90)
        lego.end_fill()
        lego.penup()
        if dievalue == random.randint(1,6):
            lego.goto(x + .75 * width, y - .25 * width)
            lego.dot(sizeofdot)
            lego.goto(x + .25 * width, y - .75 * width)
            lego.dot(sizeofdot)
            lego.goto(x + .25 * width, y - .25 * width)
            lego.dot(sizeofdot)
            lego.goto(x + .75 * width, y - .75 * width)
            lego.dot(sizeofdot)
            lego.goto(x + .25 * width, y - .50 * width)
            lego.dot(sizeofdot)
            lego.goto(x + .75 * width, y - .50 * width)
            lego.dot(sizeofdot)
            lego.goto(x + .5 * width, y - .50 * width)
            lego.dot(sizeofdot)
        # I am not able to figure out how to randomize the dots. I have been trying for a few hours but
        # every attempt i make the die are there but I am not able to get a random amount of dots in the two new squares
        
          
             
        
            
        x = x + 2.0 * width
        
            
                
            
            
                    
                    
            
            
            


            
                
            
    lego.end_fill()
#Part 3


numlessthan7 = x - 1
numgreatthan7 = x
xchances = 5
probability = xchances / (36)        
if xchances <= 7:
    print("The probability of rolling this combination is",format(numlessthan7,.4d))
elif xchances < 13:
    print("The probability of rolling this combonation is",format(numgreatthan7,.4d))

if __name__ == "__main__":
    main()
    
