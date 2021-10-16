import numpy as np

ROW_COUNT = 3
COLUMN_COUNT = 3

def create_board():
    board = np.zeros((3,3))
    board[0][0] = 1
    board[0][1] = 1
    board[0][2] = 1
    board[1][0] = 1
    board[1][1] = 0 #centre
    board[1][2] = 1
    board[2][0] = 1
    board[2][1] = 1
    board[2][2] = 1

    return board


def is_valid_move(row, col, empty_row, empty_col):
        if row == empty_row and col == empty_col:
            #return False
            print("no, this is already the empty space") #testing
        elif empty_row == 1 and empty_col == 1:
            #return True
            print("yes, empty is at centre") #testing
        elif row == 1 and col == 1:
            #return True
            print("yes, player piece is at centre") #testing
        elif col == empty_col or col + 1 == empty_col or col - 1 == empty_col:
            if row == empty_row or row + 1 == empty_row or row - 1 == empty_row:
                if col == empty_col or row == empty_row:
                    #return True
                    print("yes, adjacent") #testing
                else:
                    #return False
                    print("no, diagonal") #testing
            else:
                #return False
                print("no") #testing
        else:
            #return False
            print("no") #testing


def find_empty_pos(board):
    empty_pos = np.where(board == 0)
    empty_row = empty_pos[0]
    empty_col = empty_pos[1]
    return empty_row, empty_col #function that returns two values

board = create_board()
print(board)
game_over = False


while not game_over:
    empty_row, empty_col = find_empty_pos(board)
    print(empty_row)
    print(empty_col)

    row = int(input("Player 1 select row (0-2): "))
    col = int(input("Player 1 select column (0-2): "))

    is_valid_move(row, col, empty_row, empty_col) #note, doesnt check which tile the player is moving, make sure to add that player 1 can only move "1" tiles and player 2 can only move "2" tiles.
