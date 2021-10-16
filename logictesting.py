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

    return board

def move_piece(board, row, col, player):
    board[row][col] = player

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
    empty_row = empty_pos[0]
    empty_col = empty_pos[1]
    return empty_row, empty_col #function that returns two values

board = create_board()
print(board)
game_over = False
turn = 0


while not game_over:
    # Ask for player 1 where to move
    if turn == 0:
        empty_row, empty_col = find_empty_pos(board)
        print(empty_row)
        print(empty_col)

############## this needs to be improved ###################
        row = int(input("Player 1 select row (0-2): "))
        col = int(input("Player 1 select column (0-2): "))
        piece = board[row][col]     

        while not is_valid_move(row, col, empty_row, empty_col, 1, piece):
            print("INVALID MOVEEEE")
            row = int(input("Player 1 select row (0-2): "))
            col = int(input("Player 1 select column (0-2): "))
            piece = board[row][col]            
            is_valid_move(row, col, empty_row, empty_col, 1, piece)

        if is_valid_move(row, col, empty_row, empty_col, 1, piece):
            print("IS VALID MOVE")
############## this needs to be improved ###################


    # Ask for player 2 where to move
    else:
        empty_row, empty_col = find_empty_pos(board)
        print(empty_row)
        print(empty_col)

############## this needs to be improved ###################
        row = int(input("Player 2 select row (0-2): "))
        col = int(input("Player 2 select column (0-2): "))
        piece = board[row][col]     

        while not is_valid_move(row, col, empty_row, empty_col, 2, piece):
            print("INVALID MOVEEEE")
            row = int(input("Player 2 select row (0-2): "))
            col = int(input("Player 2 select column (0-2): "))
            piece = board[row][col]            
            is_valid_move(row, col, empty_row, empty_col, 2, piece)

        if is_valid_move(row, col, empty_row, empty_col, 2, piece):
            print("IS VALID MOVE")
############## this needs to be improved ###################

    print(board)

    turn += 1
    turn = turn % 2