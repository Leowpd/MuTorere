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

def is_valid_move(row, col, empty_row, empty_col, player, piece):
    if player == piece:
        if row == empty_row and col == empty_col:                   #this may be able to be deleted
            return False                                            #this may be able to be deleted
            #print("no, this is already the empty space") #testing  #this may be able to be deleted
        elif empty_row == 1 and empty_col == 1:
            return True
            #print("yes, empty is at centre") #testing
        elif row == 1 and col == 1:
            return True
            #print("yes, player piece is at centre") #testing
        elif col == empty_col or col + 1 == empty_col or col - 1 == empty_col:
            if row == empty_row or row + 1 == empty_row or row - 1 == empty_row:
                if col == empty_col or row == empty_row:
                    return True
                    #print("yes, adjacent") #testing
                else:
                    return False
                    #print("no, diagonal") #testing
            else:
                return False
                #print("no") #testing
        else:
            return False
            #print("no") #testing
    elif piece == 0:
        return False
        #print("no, this is already the empty space") #testing
    else:
        return False
        #print("no, you can not move your opponent's piece")
    
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
        if not is_valid_move(row, col, empty_row, empty_col, player=opponent, piece=opponent):
            #print("haha nope")
            opp_loses += 1
            #print("opp_loses", opp_loses)
        else:
            print("yup all good")
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

############## this needs to be improved ###################
        row = take_player_input(player, "row")
        col = take_player_input(player, "column")
        piece = board[row][col]     

        while not is_valid_move(row, col, empty_row, empty_col, player, piece):
            print("INVALID MOVEEEE") #testing
            row = take_player_input(player, "row")
            col = take_player_input(player, "column")
            piece = board[row][col]            
            is_valid_move(row, col, empty_row, empty_col, player, piece)

        if is_valid_move(row, col, empty_row, empty_col, player, piece):
            print("IS VALID MOVE") #testing
            move_piece(board, empty_row, empty_col, player)
            remove_piece(board, row, col)

            if winning_move(board, opponent):
                print("wtf okay you won I guess player 1")
            else:
                print("havent won yet lol player 1")

        else:
            print("something fucked up player 1")


############## this needs to be improved ###################


    # Ask for player 2 where to move
    else:
        player = 2
        opponent = 1
        empty_row, empty_col = find_empty_pos(board)

############## this needs to be improved ###################
        row = take_player_input(player, "row")
        col = take_player_input(player, "column")
        piece = board[row][col]     

        while not is_valid_move(row, col, empty_row, empty_col, player, piece):
            print("INVALID MOVEEEE") #testing
            row = take_player_input(player, "row")
            col = take_player_input(player, "column")
            piece = board[row][col]            
            is_valid_move(row, col, empty_row, empty_col, player, piece)

        if is_valid_move(row, col, empty_row, empty_col, player, piece):
            print("IS VALID MOVE") #testing
            move_piece(board, empty_row, empty_col, player)
            remove_piece(board, row, col)

            if winning_move(board, opponent):
                print("wtf okay you won I guess player 2")
            else:
                print("havent won yet lol player 2")

        else:
            print("something fucked up player 2")


############## this needs to be improved ###################

    print(board)

    turn += 1
    turn = turn % 2