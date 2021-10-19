import numpy as np

ROW_COUNT = 3
COLUMN_COUNT = 3

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    board[0][0] = 1
    board[1][0] = 1
    board[2][0] = 1
    board[2][1] = 1
    board[0][1] = 2
    board[0][2] = 2
    board[1][2] = 2
    board[2][2] = 2

    # board[0][0] = 1
    # board[1][0] = 1
    # board[2][0] = 1
    # board[2][2] = 1
    # board[0][1] = 2
    # board[0][2] = 2
    # board[1][1] = 2
    # board[1][2] = 2

    return board

def take_player_input(player, rowcol):
    n = 0
    is_int = False
    while n == 0:
        while not is_int:
            player_input = input("Player " + str(player) + " select " + str(rowcol) + " (1-3): ")
            try:
                int(player_input)
                is_int = True
            except ValueError:
                print("That is not a valid entry, please select", rowcol, "1, 2, or 3")
        player_input = int(player_input)

        if player_input < 1 or player_input > 3:
            print("That is not a valid entry, please select", rowcol, "1, 2, or 3")
            is_int = False
        else:
            n = 1
    player_input -= 1
    return player_input

def move_piece(board, empty_row, empty_col, player):
    board[empty_row][empty_col] = player

def remove_piece(board, row, col):
    board[row][col] = 0

#is the function for checking if a move is valid
def is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
    #checks if the piece a player is trying to move is actually their piece
    if player == piece_num:
        #checks if the player's piece is in the middle
        if row == 1 and col == 1:
            return True
        else:
            #checks if a player's piece is surrounded by two other of the same piece on the outside (so not including the middle piece)
            player_pieces = np.nonzero(board == player)
            list_of_player_pieces = list(zip(player_pieces[0], player_pieces[1]))
            adjacent = 0
            #checks to see if any of the player's other pieces is adjacent to the piece they are trying to move
            for piece in list_of_player_pieces:
                new_row = int(piece[0])
                new_col = int(piece[1])
                #removes the selected piece from the pieces being compared
                if col == new_col and row == new_row:
                    pass
                else:
                    #checks to see if the piece is adjacent to the selected piece
                    if col == new_col or col + 1 == new_col or col - 1 == new_col:
                        if row == new_row or row + 1 == new_row or row - 1 == new_row:
                            if row == new_row or col == new_col:
                                if not (new_row == 1 and new_col == 1):
                                    adjacent += 1
            #if there are two adjacent pieces then the selected piece cannot be moved
            if adjacent >= 2:
                return False
            else:
                #checks if the empty space is at the centre/putahi
                if empty_row == 1 and empty_col == 1:
                    return True
                #checks if the empty space is adjacent to the piece the player wants to move
                elif col == empty_col or col + 1 == empty_col or col - 1 == empty_col:
                    if row == empty_row or row + 1 == empty_row or row - 1 == empty_row:
                        if col == empty_col or row == empty_row:
                            return True
                        else:
                            return False
                            #the empty space is diagonally adjacent which is not valid
                            #this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program
                    else:
                        return False
                        #the empty space is not adjacent to the piece the player is trying to move
                        #this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program
                else:
                    return False
                    #the empty space is not adjacent to the piece the player is trying to move
                    #this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program
    #checks if the piece the player is trying to move is actually the empty space
    elif piece_num == 0:
        return False
        #selected spot is empty
        #this is here so if in the future I want to add specific error messages for why an input doesn't work, it is easy. This increases the flexibility of the program.
    else:
        return False
            #if it gets to here the player has selected their oppenent's piece, which of course is not valid
    
def find_empty_pos(board):
    empty_pos = np.where(board == 0)
    empty_row = int(empty_pos[0])
    empty_col = int(empty_pos[1])
    return empty_row, empty_col #function that returns two values

def winning_move(board, opponent):
    #print(opponent)
    opponent_pieces = np.nonzero(board == opponent)
    list_of_opp_pieces = list(zip(opponent_pieces[0], opponent_pieces[1]))
    empty_row, empty_col = find_empty_pos(board)
    opp_loses = 0

    for piece in list_of_opp_pieces:
        #print(piece)
        row = int(piece[0])
        col = int(piece[1])
        if not is_valid_move(board, row, col, empty_row, empty_col, player=opponent, piece_num=opponent):
            #print("haha nope")
            opp_loses += 1
            #print("opp_loses", opp_loses)
        else:
            pass

    #print("final opp_loses", opp_loses)
    if opp_loses == 4:
        return True
    else:
        return False


board = create_board()
print(board)
game_over = False
turn = 0


while not game_over:
    # Ask for player 1 where to move
    if turn == 0:
        player = 1
        opponent = 2
        empty_row, empty_col = find_empty_pos(board)

        row = take_player_input(player, "row")
        col = take_player_input(player, "column")
        piece_num = board[row][col]

        if is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
            print("IS VALID MOVE") #testing
            move_piece(board, empty_row, empty_col, player)
            remove_piece(board, row, col)

            if winning_move(board, opponent):
                print("wtf okay you won I guess player 1")
            else:
                print("havent won yet lol player 1")

        else:
            print("INVALID MOVE")
            turn -= 1




    # Ask for player 2 where to move
    else:
        player = 2
        opponent = 1
        empty_row, empty_col = find_empty_pos(board)

        row = take_player_input(player, "row")
        col = take_player_input(player, "column")
        piece_num = board[row][col]

        if is_valid_move(board, row, col, empty_row, empty_col, player, piece_num):
            print("IS VALID MOVE") #testing
            move_piece(board, empty_row, empty_col, player)
            remove_piece(board, row, col)

            if winning_move(board, opponent):
                print("wtf okay you won I guess player 2")
            else:
                print("havent won yet lol player 2")

        else:
            print("INVALID MOVE")
            turn -= 1



    print(board)

    turn += 1
    turn = turn % 2