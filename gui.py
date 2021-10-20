import turtle

import constants as const

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
    def start_perepere(self, pos, color):
        self.fillcolor(color)
        self.hideturtle()
        self.speed(10)
        self.shape("circle")
        self.pu()
        self.goto(const.POSITIONS[(1,1)])
        self.showturtle()
        self.speed(3)
        self.goto(pos)


def move_perepere(list_of_perepere, list_of_perepere_coords, row, col, empty_row, empty_col):
    n = -1
    for coord in list_of_perepere_coords:
        n += 1
        if coord == const.POSITIONS[(row,col)]:
            (list_of_perepere[n]).goto(const.POSITIONS[(empty_row, empty_col)])
            break




