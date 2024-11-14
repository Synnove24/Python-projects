#creates a turtle
import turtle
wn = turtle.Screen()
lol = turtle.Turtle()

#calculate angle
d = 360/7

#for loop that makes heptagon
for i in range(7):
    lol.forward(50)
    lol.left(d)
