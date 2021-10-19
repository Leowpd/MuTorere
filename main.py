import turtle

import numpy as np

import logic
import gui
import constants as const


#sets up screen
screen = turtle.Screen()
screen.setup(700, 700)


# sets the player colors, this could potentially lead to players choosing their own color.
p1color = "white"
p2color = "black"


gui.drawboard()

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
plyr2perepere1 = gui.Perepere()
plyr2perepere2 = plyr2perepere1.clone()
plyr2perepere3 = plyr2perepere1.clone()
plyr2perepere4 = plyr2perepere1.clone()
plyr1perepere1 = plyr2perepere1.clone()
plyr1perepere2 = plyr2perepere1.clone()
plyr1perepere3 = plyr2perepere1.clone()
plyr1perepere4 = plyr2perepere1.clone()
plyr2perepere1.start_perepere(const.POSITIONS[(0,1)], p2color)
plyr2perepere2.start_perepere(const.POSITIONS[(0,2)], p2color)
plyr2perepere3.start_perepere(const.POSITIONS[(1,2)], p2color)
plyr2perepere4.start_perepere(const.POSITIONS[(2,2)], p2color)
plyr1perepere1.start_perepere(const.POSITIONS[(2,1)], p1color)
plyr1perepere2.start_perepere(const.POSITIONS[(2,0)], p1color)
plyr1perepere3.start_perepere(const.POSITIONS[(1,0)], p1color)
plyr1perepere4.start_perepere(const.POSITIONS[(0,0)], p1color)

list_of_perepere = [plyr1perepere1, plyr1perepere2,
                    plyr1perepere3, plyr1perepere4,
                    plyr2perepere1, plyr2perepere2,
                    plyr2perepere3, plyr2perepere4
                    ]


# Now everything has been set up;
# the board is drawn, 
# all the perepere sprits are set up and in their starting positions, 
# and all the places a perepere can move have had their coordinates set.
# Woohoo!
# The code from this point on is the logic for the actual game playing.




# creates the board, prints the board, declares the game is not over, and sets it to player 1's turn
board = logic.create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    # Ask player 1 what piece to move
    if turn == 0:
        # declares which player is playing, which player is the opponent, and finds the empty space
        player = 1
        opponent = 2
        empty_row, empty_col = logic.find_empty_pos(board)

        # asks the player which piece they want to move, and finds what piece that is
        row = logic.take_player_input(player, "row")
        col = logic.take_player_input(player, "column")
        piece_num = board[row][col]

        # checks if a move is valid before moving the player's piece
        if logic.is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
            logic.move_piece(board, row, col, empty_row, empty_col, player)

            list_of_perepere_coords = [plyr1perepere1.pos(),
                                       plyr1perepere2.pos(),
                                       plyr1perepere3.pos(),
                                       plyr1perepere4.pos(),
                                       plyr2perepere1.pos(),
                                       plyr2perepere2.pos(),
                                       plyr2perepere3.pos(),
                                       plyr2perepere4.pos()
                                       ]
            gui.move_perepere(list_of_perepere, list_of_perepere_coords, row, col, empty_row, empty_col)

            # checks if a player has done a winning move, and if so ends the game
            if logic.winning_move(board, opponent):
                print("PLAYER 1 WINS!!")
                game_over = True

        # if a move is not valid, asks the player to make a different move and resets their turn
        else:
            print("Sorry, that move was not valid, please try again")
            turn -= 1


    # Ask player 2 what piece to move
    else:
        # declares which player is playing, which player is the opponent, and finds the empty space
        player = 2
        opponent = 1
        empty_row, empty_col = logic.find_empty_pos(board)

        # asks the player which piece they want to move, and finds what piece that is
        row = logic.take_player_input(player, "row")
        col = logic.take_player_input(player, "column")
        piece_num = board[row][col]

        # checks if a move is valid before moving the player's piece and then removing the original piece
        if logic.is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
            logic.move_piece(board, row, col, empty_row, empty_col, player)

            list_of_perepere_coords = [plyr1perepere1.pos(),
                                       plyr1perepere2.pos(),
                                       plyr1perepere3.pos(),
                                       plyr1perepere4.pos(),
                                       plyr2perepere1.pos(),
                                       plyr2perepere2.pos(),
                                       plyr2perepere3.pos(),
                                       plyr2perepere4.pos()
                                       ]
            gui.move_perepere(list_of_perepere, list_of_perepere_coords, row, col, empty_row, empty_col)

            # checks if a player has done a winning move, and if so ends the game
            if logic.winning_move(board, opponent):
                print("PLAYER 2 WINS!!")
                game_over = True

        # if a move is not valid, asks the player to make a different move and resets their turn
        else:
            print("Sorry, that move was not valid, please try again")
            turn -= 1

    # prints the board, so the players can see the board at the beginning of each turn
    print(board)

    # increments the turn by 1 and then uses mod division so that the players' turns alternate
    turn += 1
    turn = turn % 2






# thing_coords = turtle.getpos()
# search POSITION dictonary for thing_coords
# shows its position on the array
#
# for example:
#
# (turtle is at the putahi)
#
# for perepere in list_of_perepere:
#    thing_coords = turtle.getpos()
#    print(thing_coords)
#    OUTPUT: (-50.00, 50.00)
#    thing_pos = (thing that searches dictonary)
#    print(thing_pos)
#    OUTPUT: (1,1)
#    If thing_pos == row, col:
#       turtle.goto(empty_row, empty_col)
#       break



# for pos in const.POSITIONS.items():
#     if pos[1] == (-50.00, -150.00):
#         yesss = (pos[0])

# print(yesss)
