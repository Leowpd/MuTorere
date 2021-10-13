import turtle, random, time
#sets up screen
screen = turtle.Screen()
screen.setup(700, 700)

#sets the coordinates for all the places perepere can move
putahi = (-50.00,50.00)
tahi = (-50.00, 250.00)
rua = (91.42, 191.42)
toru = (150.00, 50.00)
wha = (91.42, -91.42)
rima = (-50.00, -150.00)
ono = (-191.42,-91.42)
whitu = (-250.00, 50.00)
waru = (-191.42, 191.42)

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

#class of perepere
class perepere(turtle.Turtle):
    #function to move all perepere to the starting positions
    def startperepere(self, p):
        self.hideturtle()
        self.speed(10)
        self.shape("circle")
        self.pu()
        self.goto(putahi)
        self.showturtle()
        self.speed(3)
        self.goto(p)

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
p = (-50.00, 250.00)
blackperepere1.startperepere(p)
p = (91.42, 191.42)
blackperepere2.startperepere(p)
p = (150.00, 50.00)
blackperepere3.startperepere(p)
p = (91.42, -91.42)
blackperepere4.startperepere(p)
p = (-50.00, -150.00)
whiteperepere1.startperepere(p)
p = (-191.42,-91.42)
whiteperepere2.startperepere(p)
p = (-250.00, 50.00)
whiteperepere3.startperepere(p)
p = (-191.42, 191.42)
whiteperepere4.startperepere(p)

# Now everything has been set up;
# the board is drawn, 
# all the perepere sprits are set up and in their starting positions, 
# and all the places a perepere can move have had their coordinates set.
# Woohoo!
# The code from this point on is the logic for the actual game playing.




# just for testing, makes it so the window doesnt close by itself.
screen.exitonclick()