import turtle, random, time
#sets up screen
testscreen = turtle.Screen()
testscreen.setup(700, 700)

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

#function to move all perepere to the starting positions
class perepere(turtle.Turtle):
    def startperepere(self, n):
        self.hideturtle()
        self.speed(10)
        self.shape("circle")
        self.pu()
        self.lt(90)
        self.fd(50)
        self.rt(45*n)
        self.showturtle()
        self.speed(3)
        self.fd(150)
        self.showturtle()

#creates all perepere pieces and moves them to the starting position
blackperepere1 = perepere()
blackperepere1.fillcolor("black")
blackperepere2 = blackperepere1.clone()
blackperepere2.fillcolor("black")
blackperepere3 = blackperepere1.clone()
blackperepere3.fillcolor("black")
blackperepere4 = blackperepere1.clone()
blackperepere4.fillcolor("black")
whiteperepere1 = blackperepere1.clone()
whiteperepere1.fillcolor("white")
whiteperepere2 = blackperepere1.clone()
whiteperepere2.fillcolor("white")
whiteperepere3 = blackperepere1.clone()
whiteperepere3.fillcolor("white")
whiteperepere4 = blackperepere1.clone()
whiteperepere4.fillcolor("white")
n=1
blackperepere1.startperepere(n)
n=n+1
blackperepere2.startperepere(n)
n=n+1
blackperepere3.startperepere(n)
n=n+1
blackperepere4.startperepere(n)
n=n+1
whiteperepere1.startperepere(n)
n=n+1
whiteperepere2.startperepere(n)
n=n+1
whiteperepere3.startperepere(n)
n=n+1
whiteperepere4.startperepere(n)

kore = (-50.00,50.00)
rua = (106.07,156.07)

blackperepere1.goto(kore)
blackperepere2.goto(rua)

# just for testing, makes it so the window doesnt close by itself, the window closes when it is clicked on.
testscreen.exitonclick()

# Positions of each spot NOPE ACTUALLY ALL THESE ARE WRONG ARGGGGGGGG FUCKKKKKKK
# kore  (0)  (-50.00,50.00)
# tahi  (1)  (-0.00,200.00)
# rua   (2)  (106.07,156.07)
# toru  (3)  (150.00,50.00)
# wha   (4)  (106.07,-56.07)
# rima  (5)  (0.00,-100.00)
# ono   (6)  (-106.07,-56.07)
# whitu (7)  (-150.00,50.00)
# waru  (8)  (-106.07,156.07)
# so all the above are wrong which sucks. Its because each turtle is oriented differently, for this
# to work im gonna need all turtles facing in the same direction (ill just go with right cause thats
# the default) and then ill make them goto the coordinate of each spot (ill have to re-figure out all
# the spots). But i like the cool animation at the beginning so one by one ill make them invisiable and
# go to the centre, then make them visible and make them go to their respective spots.

