import numpy as np

BOARD_SETUP = [[1.0, 2.0, 2.0], [1.0, 0.0, 2.0], [1.0, 1.0, 2.0]]


# function that creates the board
def create_board():
    board = np.array(BOARD_SETUP)
    return board


# function that takes the player's input for row or column
def take_player_input(player, rowcol):
    n = 0
    is_int = False
    while n == 0:  # loops until the player makes a valid entry

        while not is_int:  # loops until a player enters an interger
            player_input = input(
                "Player " + str(player) + " select " + str(rowcol) + " (1-3): "
            )
            try:  # uses try except to reject non-interger entries and asks the player to try again
                int(player_input)
                is_int = True
            except ValueError:
                print("That is not a valid entry, please select", rowcol, "1, 2, or 3")
        player_input = int(player_input)

        # checks if the player's interger input is 1, 2, or 3
        if player_input < 1 or player_input > 3:
            print("That is not a valid entry, please select", rowcol, "1, 2, or 3")
            is_int = False
            # repeats the loop if the entry in not valid
        else:
            # ends the loops when the player makes a valid entry
            n = 1
    player_input -= 1  # reduces player input by 1 as the rest of the logic uses the board's rows and columns as (0, 1, 2) not (1, 2, 3)
    return player_input


# function for moving a piece
def move_piece(board, empty_row, empty_col, player):
    # sets the position of the empty space to the player's piece
    board[empty_row][empty_col] = player


# function for removing a piece
def remove_piece(board, row, col):
    # sets the spot the piece was formally to zero (empty)
    board[row][col] = 0


# function for checking if a move is valid
def is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
    # checks if the piece a player is trying to move is actually their piece
    if player == piece_num:
        # checks if the player's piece is in the middle
        if row == 1 and col == 1:
            return True
        else:
            # checks if a player's piece is surrounded by two other of the same piece on the outside (so not including the middle piece)
            player_pieces = np.nonzero(board == player)
            list_of_player_pieces = list(zip(player_pieces[0], player_pieces[1]))
            adjacent = 0
            # checks to see if any of the player's other pieces is adjacent to the piece they are trying to move
            for piece in list_of_player_pieces:
                new_row = int(piece[0])
                new_col = int(piece[1])
                # removes the selected piece from the pieces being compared
                if col == new_col and row == new_row:
                    pass
                else:
                    # checks to see if the piece is adjacent to the selected piece
                    if col == new_col or col + 1 == new_col or col - 1 == new_col:
                        if row == new_row or row + 1 == new_row or row - 1 == new_row:
                            if row == new_row or col == new_col:
                                if not (new_row == 1 and new_col == 1):
                                    adjacent += 1
            # if there are two adjacent pieces then the selected piece cannot be moved
            if adjacent >= 2:
                return False
            else:
                # checks if the empty space is at the centre/putahi
                if empty_row == 1 and empty_col == 1:
                    return True
                # checks if the empty space is adjacent to the piece the player wants to move
                elif col == empty_col or col + 1 == empty_col or col - 1 == empty_col:
                    if row == empty_row or row + 1 == empty_row or row - 1 == empty_row:
                        if col == empty_col or row == empty_row:
                            return True
                        else:
                            return False
                            # the empty space is diagonally adjacent which is not valid
                            # this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program
                    else:
                        return False
                        # the empty space is not adjacent to the piece the player is trying to move
                        # this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program
                else:
                    return False
                    # the empty space is not adjacent to the piece the player is trying to move
                    # this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program
    # checks if the piece the player is trying to move is actually the empty space
    elif piece_num == 0:
        return False
        # selected spot is empty
        # this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program.
    else:
        return False
        # if it gets to here the player has selected their oppenent's piece, which of course is not valid


# function for finding the empty position on the board
def find_empty_pos(board):
    empty_pos = np.where(board == 0)
    empty_row = int(empty_pos[0])
    empty_col = int(empty_pos[1])
    # returns the row and column of the empty space
    return empty_row, empty_col


# function for checking if a move is a winning move
def winning_move(board, opponent):
    # finds all the opponent's pieces and the empty space
    opponent_pieces = np.nonzero(board == opponent)
    list_of_opp_pieces = list(zip(opponent_pieces[0], opponent_pieces[1]))
    empty_row, empty_col = find_empty_pos(board)
    # variable for how many of the opponent's pieces are unable to move, sets this to zero
    opp_loses = 0

    # loops through each of the opponent's pieces to check if they are able to move
    for piece in list_of_opp_pieces:
        # sets "row" and "col" to one of the opponent's pieces
        row = int(piece[0])
        col = int(piece[1])
        # calls the is_valid_move function to check if that piece is able to move, if not opp_loses is incremented by 1
        if not is_valid_move(
            board, row, col, empty_row, empty_col, player=opponent, piece_num=opponent
        ):
            opp_loses += 1

    # if all four of the opponent's pieces are unable to be moved, winning_move returns True, otherwise the function returns False
    if opp_loses == 4:
        return True
    else:
        return False


# creates the board, prints the board, declares the game is not over, and sets it to player 1's turn
board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    # Ask player 1 what piece to move
    if turn == 0:
        # declares which player is playing, which player is the opponent, and finds the empty space
        player = 1
        opponent = 2
        empty_row, empty_col = find_empty_pos(board)

        # asks the player which piece they want to move, and finds what piece that is
        row = take_player_input(player, "row")
        col = take_player_input(player, "column")
        piece_num = board[row][col]

        # checks if a move is valid before moving the player's piece and then removing the original piece
        if is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
            move_piece(board, empty_row, empty_col, player)
            remove_piece(board, row, col)

            # checks if a player has done a winning move, and if so ends the game
            if winning_move(board, opponent):
                print("PLAYER 2 WINS!!")
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
        empty_row, empty_col = find_empty_pos(board)

        # asks the player which piece they want to move, and finds what piece that is
        row = take_player_input(player, "row")
        col = take_player_input(player, "column")
        piece_num = board[row][col]

        # checks if a move is valid before moving the player's piece and then removing the original piece
        if is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
            move_piece(board, empty_row, empty_col, player)
            remove_piece(board, row, col)

            # checks if a player has done a winning move, and if so ends the game
            if winning_move(board, opponent):
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
