# A simple python project made by Thegr8kabeer that uses the 'Turtle' module.
# Easy to understand syntax for the person who knows the basics of Turtle.
# Feel free to edit my code and do some experiments!!!
# Don't forget to follow me on instagram at https://instagram.com/thegr8kabeer/

import turtle

turtle_1 = turtle.Turtle()
# You can chamge the speed of the turtle by writing in the paranthesis below.
turtle_1.speed(5) 

# Making the function that determines how and where the 'turtle' moves. 
def square():
    # Moves forward
    turtle_1.forward(100)
    # Moves right
    turtle_1.right(90)
    # Moves forward
    turtle_1.forward(100)
    # Moves right
    turtle_1.right(90)
    # Moves forward
    turtle_1.forward(100)
    # Moves right
    turtle_1.right(90)
    # Moves forward
    turtle_1.forward(100)

# Making a for loop to determine how many joint squares do you want.
for count in range(4):
    square()

# To exit , just press any key
input("Press any key to exit ...")
