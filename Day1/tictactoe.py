import copy

def initial_state():
    return [[None, None, None], [None, None, None], [None, None, None]]
def player(board):
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            if cell == "O":
                o_count += 1
    if x_count == o_count:
        return "X"
    else:
        return "O"
def actions(board):
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] is None:
                moves.append((r, c))
    return moves
def result(board, action):
    new_board = copy.deepcopy(board)
    r, c = action
    new_board[r][c] = player(board)
    return new_board
def winner(board):
    lines = []
    for r in range(3):
        lines.append([board[r][0], board[r][1], board[r][2]])
    for c in range(3):
        lines.append([board[0][c], board[1][c], board[2][c]])
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    for line in lines:
        if line[0] is not None and line[0] == line[1] == line[2]:
            return line[0]
    return None
def terminal(board):
    if winner(board) is not None:
        return True
    if len(actions(board)) == 0:
        return True
    return False
def utility(board):
    win = winner(board)
    if win == "X":
        return 1
    if win == "O":
        return -1
    return 0
def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -float("inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v
def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v
def minimax(board):
    if terminal(board):
        return None
    alpha = -float("inf")
    beta = float("inf")
    if player(board) == "X":
        best_value = -float("inf")
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action), alpha, beta)
            if value > best_value:
                best_value = value
                best_move = action
            alpha = max(alpha, best_value)
        return best_move
    else:
        best_value = float("inf")
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action), alpha, beta)
            if value < best_value:
                best_value = value
                best_move = action
            beta = min(beta, best_value)
        return best_move