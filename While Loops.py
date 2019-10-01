 
linelength = 1
import turtle
while linelength != 0:
    
    pencolor=input("what colour do you want the pen to be? ")
    linelength=input("how long do you want your line to be? ")
    angle=input("what angle would you like to draw? ")   
    turtle.pencolor(pencolor)
    turtle.right(float(angle))
    turtle.forward(float(linelength))
print("thanks for playing")
