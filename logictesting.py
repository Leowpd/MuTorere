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

def move_piece(board, row, col, player):
    board[row][col] = player

def remove_piece(board, row, col):
    board[row][col] = 0

def is_valid_move(board, row, col):
    return board[row][col] == 0


board = create_board()
print(board)
game_over = False
turn = 0


while not game_over:
    # Ask for player 1 where to move
    if turn == 0:
        row = int(input("Player 1 select row (0-2): "))
        col = int(input("Player 1 select column (0-2): "))

        if is_valid_move(board, row, col):
            move_piece(board, row, col, 1)
        else:
            print("invalid move")


    # Ask for player 2 where to move
    else:
        row = int(input("Player 2 select row (0-2): "))
        col = int(input("Player 2 select column (0-2): "))

        if is_valid_move(board, row, col):
            move_piece(board, row, col, 2)
        else:
            print("invalid move")

    print(board)

    turn += 1
    turn = turn % 2