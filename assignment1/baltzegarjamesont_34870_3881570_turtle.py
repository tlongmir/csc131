import turtle
import random 
def main():
    min = 1
    max = 6
    turtle.setup(2650,1440)
    win = turtle.Screen()
    win.bgcolor("blue")
    dice_value = 0
    bob = turtle.Turtle()
    bob.fillcolor("white")
    bob.begin_fill()
    bob.penup()
    bob.goto(-800,0)
    width = 100
    bob.dot(16, "Black")
    for i in range(6):
        bob.fillcolor("white")
        bob.fd(width)
        bob.left(90)
        bob.fd(width)
        bob.left(90)
        bob.fd(width)
        bob.left(90)
        bob.fd(width)
        bob.penup()
        bob.left(90)
        bob.fd(300)        
    bob.end_fill()
    

    
        
        
        
        
if __name__ == "__main__":
    main()

