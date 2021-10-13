import turtle, random, time
#sets up screen
screen = turtle.Screen()
screen.setup(700, 700)

#draws the board
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


drawboard()






# just for testing, makes it so the window doesnt close by itself.
screen.exitonclick()