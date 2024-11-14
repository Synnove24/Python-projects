#asks users for inputs
sl = int(input("What is the side length?"))
sn = int(input("How many sides?"))

#Gets a turtle
import turtle
wn = turtle.Screen()
sam = turtle.Turtle()

#calculates the angle
a = 360/sn

#Turtle draws shape
for i in range(sn):
    sam.forward(sl)
    sam.left(a)
