from tictactoe import *

board = initial_state()
while not terminal(board):
    if player(board) == "O":
        row, col = map(int, input("row,col: ").split(","))
        board = result(board, (row, col))
    else:
        board = result(board, minimax(board))
    print(board)
print("Winner:", winner(board))