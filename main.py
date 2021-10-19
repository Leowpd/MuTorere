import turtle
import random
import time

import numpy as np

import logic as lg
import constants as const


#sets up screen
screen = turtle.Screen()
screen.setup(700, 700)


# sets the player colors, this could potentially lead to players choosing their own color.
P1COLOR = "white"
P2COLOR = "black"


# function draws the board
def drawboard():
    #draws one kewai
    def kewai():
        t.pd()
        t.rt(172)
        t.fd(150)
        t.pu()
        t.fd(10)
        t.pd()
        t.rt(98)
        t.pu()
        t.fd(44.5)
        t.pd()
        t.rt(98)
        t.pu()
        t.fd(10)
        t.pd()
        t.fd(150)

    t = turtle.Turtle(visible=False)
    t.width(2)
    t.speed(0)
    t.color("black")
    t.lt(90)
    t.pu()
    t.fd(250)
    t.pd()

    #draws 8 kewai
    for i in range(8):
        kewai()
        t.pu()
        t.rt(172)
        t.fd(200)
        t.rt(180)
        t.rt(45)
        t.fd(200)
    t.rt(180)
    t.fd(245)
    t.lt(90)
    t.pd()
    t.circle(45)
    t.pu()
    t.rt(90)
    t.fd(155)
    t.lt(90)
    t.width(1)
    t.pd()
    t.circle(200)


#class of Perepere
class Perepere(turtle.Turtle):
    #function to move all perepere to the starting positions
    def startperepere(self, pos, color):
        self.fillcolor(color)
        self.hideturtle()
        self.speed(10)
        self.shape("circle")
        self.pu()
        self.goto(const.POSITIONS[(1,1)])
        self.showturtle()
        self.speed(3)
        self.goto(pos)


drawboard()

#draws the shape of the perepere (a circle) that all the perepere turtles will use
drawcircle = turtle.Turtle()
drawcircle.hideturtle()
drawcircle.speed(10)
drawcircle.pu()
drawcircle.lt(90)
drawcircle.fd(80)
drawcircle.lt(90)
drawcircle.pd()
drawcircle.begin_poly() 
drawcircle.circle(30)
turtle.end_poly()
circle = drawcircle.get_poly()
turtle.register_shape("circle", circle)
turtle.hideturtle()
drawcircle.clear()


#creates all perepere pieces and moves them to the starting position
blackperepere1 = Perepere()
blackperepere2 = blackperepere1.clone()
blackperepere3 = blackperepere1.clone()
blackperepere4 = blackperepere1.clone()
whiteperepere1 = blackperepere1.clone()
whiteperepere2 = blackperepere1.clone()
whiteperepere3 = blackperepere1.clone()
whiteperepere4 = blackperepere1.clone()
blackperepere1.startperepere(const.POSITIONS[(0,1)], P2COLOR)
blackperepere2.startperepere(const.POSITIONS[(0,2)], P2COLOR)
blackperepere3.startperepere(const.POSITIONS[(1,2)], P2COLOR)
blackperepere4.startperepere(const.POSITIONS[(2,2)], P2COLOR)
whiteperepere1.startperepere(const.POSITIONS[(2,1)], P1COLOR)
whiteperepere2.startperepere(const.POSITIONS[(2,0)], P1COLOR)
whiteperepere3.startperepere(const.POSITIONS[(1,0)], P1COLOR)
whiteperepere4.startperepere(const.POSITIONS[(0,0)], P1COLOR)


# Now everything has been set up;
# the board is drawn, 
# all the perepere sprits are set up and in their starting positions, 
# and all the places a perepere can move have had their coordinates set.
# Woohoo!
# The code from this point on is the logic for the actual game playing.






# just for testing, makes it so the window doesnt close by itself.
screen.exitonclick()