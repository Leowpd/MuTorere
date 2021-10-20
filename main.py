import turtle
import time

import logic
import gui
import constants as const


# This is the script file that is meant to be run
if __name__ == "__main__":

    # function that takes the player's input for row or column
    def take_player_input(player):
        n = 0
        is_int = False
        while n == 0:  # loops until the player makes a valid entry

            while not is_int:  # loops until a player enters an interger
                player_input = input(
                    "Player " + str(player) + " select piece you wish to move (0-8): "
                )
                # uses try except to reject non-interger entries and asks the
                # player to try again
                try:
                    int(player_input)
                    is_int = True
                except ValueError:
                    print(const.ERROR_MESSAGE)
            player_input = int(player_input)

            # checks if the player's interger input is 1, 2, or 3
            if player_input < 0 or player_input > 8:
                print(const.ERROR_MESSAGE)
                is_int = False
                # repeats the loop if the entry in not valid
            else:
                # ends the loops when the player makes a valid entry
                n = 1
        row, col = const.LABEL_TO_POS[player_input]
        return row, col

    # function that plays a player's turn
    def player_turn(player, opponent, turn):
        empty_row, empty_col = logic.find_empty_pos(board)

        # asks the player which piece they want to move, and finds what piece
        # that is
        row, col = take_player_input(player)
        piece_num = board[row][col]

        # checks if a move is valid before moving the player's piece
        if logic.is_valid_move(
            board, row, col, empty_row, empty_col, player, piece_num
        ):
            logic.move_piece(board, row, col, empty_row, empty_col, player)

            list_of_perepere_coords = [
                plyr1perepere1.get_coords(),
                plyr1perepere2.get_coords(),
                plyr1perepere3.get_coords(),
                plyr1perepere4.get_coords(),
                plyr2perepere1.get_coords(),
                plyr2perepere2.get_coords(),
                plyr2perepere3.get_coords(),
                plyr2perepere4.get_coords(),
            ]
            gui.move_perepere(
                list_of_perepere,
                list_of_perepere_coords,
                row,
                col,
                empty_row,
                empty_col,
            )

            turn = turn

            # checks if a player has done a winning move, and if so
            # ends the game
            if logic.winning_move(board, opponent):
                winning_message = "PLAYER " + str(player) + " WINS!"
                print(winning_message)
                t = turtle.Turtle()
                t.hideturtle()
                t.pu()
                t.speed(0)
                t.goto(-260, 90)
                t.write(winning_message, font=("Arial", 50, "normal"))
                time.sleep(3)
                t.clear()
                game_over = True
            else:
                game_over = False

        # if a move is not valid, asks the player to make a different move
        # and resets their turn
        else:
            print("Sorry, that move was not valid, please try again")
            turn -= 1
            game_over = False
        return turn, game_over

    print("Welcome to Mū Tōrere!")

    # sets up screen
    screen = turtle.Screen()
    screen.setup(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
    screen.title("Mū Tōrere")

    gui.draw_board()

    # draws the shape of the perepere (a circle) that all the
    # perepere turtles will use
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

    # creates all perepere pieces and moves them to the starting position
    plyr2perepere1 = gui.Perepere(const.POSITIONS[(0, 1)], const.P2COLOR)
    plyr2perepere2 = gui.Perepere(const.POSITIONS[(0, 2)], const.P2COLOR)
    plyr2perepere3 = gui.Perepere(const.POSITIONS[(1, 2)], const.P2COLOR)
    plyr2perepere4 = gui.Perepere(const.POSITIONS[(2, 2)], const.P2COLOR)
    plyr1perepere1 = gui.Perepere(const.POSITIONS[(2, 1)], const.P1COLOR)
    plyr1perepere2 = gui.Perepere(const.POSITIONS[(2, 0)], const.P1COLOR)
    plyr1perepere3 = gui.Perepere(const.POSITIONS[(1, 0)], const.P1COLOR)
    plyr1perepere4 = gui.Perepere(const.POSITIONS[(0, 0)], const.P1COLOR)

    list_of_perepere = [
        plyr1perepere1,
        plyr1perepere2,
        plyr1perepere3,
        plyr1perepere4,
        plyr2perepere1,
        plyr2perepere2,
        plyr2perepere3,
        plyr2perepere4,
    ]

    playing = True

    while playing:
        # creates the board, prints the board, declares the game is not over,
        # and sets it to player 1's turn
        board = logic.create_board()
        game_over = False
        turn = 0

        while not game_over:
            # Ask player 1 what piece to move
            if turn == 0:
                # declares which player is playing, which player is the
                # opponent and finds the empty space
                player = 1
                opponent = 2
                turn, game_over = player_turn(player, opponent, turn)

            # Ask player 2 what piece to move
            else:
                # declares which player is playing, which player is the
                # opponent, and finds the empty space
                player = 2
                opponent = 1
                turn, game_over = player_turn(player, opponent, turn)

            # prints the board, so the players can see the board at the
            # beginning of each turn

            # increments the turn by 1 and then uses mod division so that the
            # players' turns alternate
            turn += 1
            turn = turn % 2

        play_again = input("Would you like to play again? (Yes/No) ")
        if play_again.lower() == "yes" or play_again.lower() == "y":
            playing = True
            plyr2perepere1.go_to_pos(const.POSITIONS[(0, 1)])
            plyr2perepere2.go_to_pos(const.POSITIONS[(0, 2)])
            plyr2perepere3.go_to_pos(const.POSITIONS[(1, 2)])
            plyr2perepere4.go_to_pos(const.POSITIONS[(2, 2)])
            plyr1perepere1.go_to_pos(const.POSITIONS[(2, 1)])
            plyr1perepere2.go_to_pos(const.POSITIONS[(2, 0)])
            plyr1perepere3.go_to_pos(const.POSITIONS[(1, 0)])
            plyr1perepere4.go_to_pos(const.POSITIONS[(0, 0)])
        else:
            playing = False
