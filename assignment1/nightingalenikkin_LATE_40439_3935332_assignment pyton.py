#Name: Nikki Nightingale
#Date: 3/4/2021
#Program Name: Random Dice
#Description: Creating dice and randomizing the dice varaible.

import turtle
import random



def main():

    turtle.setup(800,600)
    win = turtle.Screen()
    win.bgcolor("Blue")

    Ty =turtle.Turtle()

    Ty.penup()
    Ty.pendown()
    Ty.fillcolor("White")
    Ty.begin_fill()
    
   

    DiceNum = (1,6)
    dicesize = 100
    dotwidth = (dicesize // 6)
    x = -400 
    y = 300


    for c in range(1):

        Ty.forward(100)
        Ty.right(90)
        Ty.forward(100)
        Ty.right(90)
        Ty.forward(100)
        Ty.right(90)
        Ty.forward(100)
        Ty.right(90) 
        Ty.penup()
        Ty.goto(x + (1.5 * dicesize) , y)
        Ty.end_fill()

        DiceNum = 1

        if DiceNum == 1:
                
            Ty.dot(dotwidth, "black")

        elif DiceNum == 2:

            Ty.dot(dotwidth, "black")

        elif DiceNum == 3:

            Ty.dot(dotwidth,  "black")
                                        

        elif DiceNum == 4:

            Ty.dot(dotwidth, "black")

        elif DiceNum == 5:

            Ty.dot(dotwidth, "black")

        elif DiceNum == 6:

            Ty.dot(dotwidth,  "black")

        else:

            None
            

        for d in range(1):

            
            Ty.begin_fill()
            Ty.pendown()
            Ty.forward(100)
            Ty.right(90)
            Ty.forward(100)
            Ty.right(90)
            Ty.forward(100)
            Ty.right(90)
            Ty.forward(100)
            Ty.right(90) 
            Ty.penup()
            Ty.goto(x + (1.5 * dicesize) * 2, y)
            Ty.end_fill()

            DiceNum = 2

            if DiceNum == 1:
                
                Ty.dot(dotwidth, "black")
 

            elif DiceNum == 2:

                Ty.dot(dotwidth , "black")
                Ty.dot(dotwidth , "black")


            elif DiceNum == 3:

                Ty.dot(dotwidth,  "black")
                                        

            elif DiceNum == 4:

                Ty.dot(dotwidth, "black")

            elif DiceNum == 5:

                Ty.dot(dotwidth, "black")

            elif DiceNum == 6:

                Ty.dot(dotwidth, "black")

            else:

                None
 
         

            for e in range(1):
                
                Ty.begin_fill()
                Ty.pendown()
                Ty.forward(100)
                Ty.right(90)
                Ty.forward(100)
                Ty.right(90)
                Ty.forward(100)
                Ty.right(90)
                Ty.forward(100)
                Ty.right(90) 
                Ty.penup()
                Ty.goto(x + (1.5 * dicesize) * 3, y)
                Ty.end_fill()

                DiceNum = 3

                if DiceNum == 1:
                
                    Ty.dot(dotwidth, "black")


                elif DiceNum == 2:

                    Ty.dot(dotwidth, "black")

                elif DiceNum == 3:

                    Ty.dot(dotwidth, "black")
                    Ty.dot(dotwidth, "black")
                    Ty.dot(dotwidth, "black")
                                        

                elif DiceNum == 4:

                    Ty.dot(dotwidth, "black")

                elif DiceNum == 5:

                    Ty.dot(dotwidth, "black")

                elif DiceNum == 6:

                    Ty.dot(dotwidth, "black")

                else:

                    None

                for f in range(1):

                    DiceNum = 4

                    Ty.begin_fill()
                    Ty.pendown() 
                    Ty.forward(100)
                    Ty.right(90)
                    Ty.forward(100)
                    Ty.right(90)
                    Ty.forward(100)
                    Ty.right(90)
                    Ty.forward(100)
                    Ty.right(90) 
                    Ty.penup()
                    Ty.goto(x + (1.5 * dicesize) * 4, y)
                    Ty.end_fill()

                    if DiceNum == 1:
                
                        Ty.dot(dotwidth, "black")
 

                    elif DiceNum == 2:

                        Ty.dot(dotwidth, "black")

                    elif DiceNum == 3:

                        Ty.dot(dotwidth, "black")
                                        

                    elif DiceNum == 4:

                        Ty.dot(dotwidth, "black")
                        Ty.dot(dotwidth, "black")
                        Ty.dot(dotwidth, "black")
                        Ty.dot(dotwidth, "black")

                    elif DiceNum == 5:

                        Ty.dot(dotwidth, "black")

                    elif DiceNum == 6:

                        Ty.dot(dotwidth, "black")

                    else:

                        None
                    
                    for g in range(1):

    
                        Ty.begin_fill()
                        Ty.pendown() 
                        Ty.forward(100)
                        Ty.right(90)
                        Ty.forward(100)
                        Ty.right(90)
                        Ty.forward(100)
                        Ty.right(90)
                        Ty.forward(100)
                        Ty.right(90) 
                        Ty.penup()
                        Ty.goto(x + (1.5 * dicesize) * 5, y)
                        Ty.end_fill()

                        DiceNum = 5

                        if DiceNum == 1:
                
                            Ty.dot(dotwidth, "black")


                        elif DiceNum == 2:

                            Ty.dot(dotwidth, "black")

                        elif DiceNum == 3:

                            Ty.dot(dotwidth, "black")
                                        

                        elif DiceNum == 4:

                            Ty.dot(dotwidth, "black")

                        elif DiceNum == 5:

                            Ty.dot(dotwidth, "black")
                            Ty.dot(dotwidth, "black")
                            Ty.dot(dotwidth, "black")
                            Ty.dot(dotwidth, "black")
                            Ty.dot(dotwidth, "black")

                        elif DiceNum == 6:

                            Ty.dot(dotwidth,  "black")

                        else:

                            None 
                    

                        for h in range(1):
                            
                            Ty.begin_fill()
                            Ty.pendown() 
                            Ty.forward(100)
                            Ty.right(90)
                            Ty.forward(100)
                            Ty.right(90)
                            Ty.forward(100)
                            Ty.right(90)
                            Ty.forward(100)
                            Ty.right(90) 
                            Ty.penup()
                            Ty.goto(x + (1.5 * dicesize) * 6, y)
                            Ty.pendown()
                            Ty.end_fill()

                            DiceNum = 6

                            if DiceNum == 1:
                
                                Ty.dot(dotwidth, "black")
 

                            elif DiceNum == 2:

                                Ty.dot(dotwidth, "black")

                            elif DiceNum == 3:

                                Ty.dot(dotwidth, "black")
                                        
                            elif DiceNum == 4:

                                Ty.dot(dotwidth, "black")

                            elif DiceNum == 5:

                                Ty.dot(dotwidth, "black")

                            elif DiceNum == 6:

                                Ty.dot(dotwidth, "black")
                                Ty.dot(dotwidth, "black")
                                Ty.dot(dotwidth, "black")
                                Ty.dot(dotwidth, "black")
                                Ty.dot(dotwidth, "black")
                                Ty.dot(dotwidth, "black")

                            else:

                                None 

                            for i in range(1):

                                Ty.begin_fill()
                                Ty.pendown() 
                                Ty.forward(100)
                                Ty.right(90)
                                Ty.forward(100)
                                Ty.right(90)
                                Ty.forward(100)
                                Ty.right(90)
                                Ty.forward(100)
                                Ty.right(90) 
                                Ty.penup()
                                Ty.goto(x +10 , y)
                                Ty.pendown()
                                Ty.end_fill()

                                for h in range(1):

                                    Ty.begin_fill()
                                    Ty.pendown() 
                                    Ty.forward(100)
                                    Ty.right(90)
                                    Ty.forward(100)
                                    Ty.right(90)
                                    Ty.forward(100)
                                    Ty.right(90)
                                    Ty.forward(100)
                                    Ty.right(90) 
                                    Ty.penup()
                                    Ty.pendown()

                                                                       

                                        

                



    Ty.end_fill()   
    turtle.mainloop()




if __name__ == "__main__":
    main()

        

    
