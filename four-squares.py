# A simple python project made by Thegr8kabeer that uses the 'Turtle' module
# Easy to understand syntax for the person who knows the basics of Turtle
# Feel free to edit my code and do some experiments!!!
# Don't forget to follow me on instagram at https://instagram.com/thegr8kabeer/

import turtle

turtle_1 = turtle.Turtle()
#You can  in the parentheses, if would change the speed of the turtle
turtle_1.speed(5) 

def square():
    turtle_1.forward(100)
    turtle_1.right(90)
    turtle_1.forward(100)
    turtle_1.right(90)
    turtle_1.forward(100)
    turtle_1.right(90)
    turtle_1.forward(100)

for count in range(4):
    square()

input("Press any key to exit ...")