import turtle

import constants as const

# function draws the board
def draw_board():
    # draws one kewai
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

    # sets up the turtle used for drawing the board
    t = turtle.Turtle(visible=False)
    t.width(2)
    t.speed(0)
    t.color("black")
    t.lt(90)
    t.pu()
    t.fd(250)
    t.pd()

    # draws 8 kewai
    for i in range(8):
        kewai()
        t.pu()
        t.rt(172)
        t.fd(200)
        t.rt(180)
        t.rt(45)
        t.fd(200)
    # finished off the board
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

    # Places all the labels for the positions
    t.setheading(180)
    t.pu()
    t.goto(const.LABELS["Tahi"])
    t.write("Tahi (1)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Rua"])
    t.write("Rua (2)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Toru"])
    t.write("Toru (3)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Wha"])
    t.write("Whā (4)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Rima"])
    t.write("Rima (5)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Ono"])
    t.write("Ono (6)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Whitu"])
    t.write("Whitu (7)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Waru"])
    t.write("Waru (8)", font=("Arial", 16, "normal"))
    t.goto(const.LABELS["Putahi"])
    t.write("Pūtahi/Centre (0)", font=("Arial", 16, "normal"))


# class of Perepere
class Perepere(turtle.Turtle):
    def __init__(self, pos, color):
        self.turtle = turtle.Turtle()
        self.turtle.fillcolor(color)
        self.turtle.hideturtle()
        self.turtle.speed(10)
        self.turtle.shape("circle")
        self.turtle.pu()
        self.turtle.goto(const.POSITIONS[(1, 1)])
        self.turtle.showturtle()
        self.turtle.speed(3)
        self.turtle.goto(pos)

    # function for Perepere to get coords
    def get_coords(self):
        coords = self.turtle.pos()
        return coords

    # function for Perepere to go to a position
    def go_to_pos(self, pos):
        self.turtle.goto(pos)

# function that moves the selected perepere to the empty space
def move_perepere(
    list_of_perepere, list_of_perepere_coords, row, col, empty_row, empty_col
):
    n = -1
    for coord in list_of_perepere_coords:
        n += 1
        if coord == const.POSITIONS[(row, col)]:
            (list_of_perepere[n]).go_to_pos(const.POSITIONS[(empty_row, empty_col)])
            break
