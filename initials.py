"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.

"""

__author__ = "Roshani Ghimire"

import turtle


def main():
    painter = turtle.Turtle() # The turtle graphics object

    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    
   
    painter.speed(2)
    
    #Positioning the pointer
    painter.penup()
    painter.left(180)
    painter.forward(150)
    painter.right(90)
    
    #Starting to draw Initial: R
    painter.pendown()
    painter.forward(180)
    painter.right(90)
    painter.forward(90)
    painter.right(90)
    painter.forward(90)
    painter.right(90)
    painter.forward(90)
    painter.left(135)
    painter.forward(127.28)
    
     #Initial: G
    painter.penup()
    painter.left(45)
    painter.left(50)
    painter.forward(230)
    painter.right(50)
    painter.pendown()
    painter.backward(90)
    painter.left(90)
    painter.backward(180)
    painter.right(90)
    painter.forward(90)
    painter.left(90)
    painter.forward(60)
    painter.right(90)
    painter.backward(30)
    painter.forward(60)
    
    # Avoid closing the window automatically
    painter.screen.mainloop()


if __name__ == "__main__":
    main()
