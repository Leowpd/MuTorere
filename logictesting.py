import numpy as np

ROW_COUNT = 3
COLUMN_COUNT = 3

def create_board():
    board = np.zeros((3,3))

    board[0][0] = 1
    board[1][0] = 1
    board[2][0] = 1
    board[2][1] = 1

    board[0][1] = 2
    board[0][2] = 2
    board[1][2] = 2
    board[2][2] = 2

    return board

board = create_board()
print(board)