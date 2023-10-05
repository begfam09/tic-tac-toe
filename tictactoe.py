"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for row in board:
        for cell in row:
            if cell == 'X':
                count_x += 1
            elif cell == 'O':
                count_o += 1

    if count_x > count_o:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_actions = set()

    for r_index, row in enumerate(board):
        for c_index, col in enumerate(row):
            if col is EMPTY:
                set_actions.add((r_index, c_index))
    
    return set_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)

    row = action[0]
    col = action[1]

    new_board[row][col] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    candidates = []
    candidates.append([board[0][0], board[0][1], board[0][2]])
    candidates.append([board[1][0], board[1][1], board[1][2]])
    candidates.append([board[2][0], board[2][1], board[2][2]])
    candidates.append([board[0][0], board[1][0], board[2][0]])
    candidates.append([board[0][1], board[1][1], board[2][1]])
    candidates.append([board[0][2], board[1][2], board[2][2]])
    candidates.append([board[0][0], board[1][1], board[2][2]])
    candidates.append([board[2][0], board[1][1], board[0][2]])

    for candidate in candidates:
        if candidate[0] == candidate[1] == candidate[2]:
            if candidate[0] is not EMPTY:
                return candidate[0]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in (X, O):
        return True

    for row in board:
        for col in row:
            if col is EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    action_set = actions(board)

    if player(board) == X:
        v = -math.inf
        for action in action_set:
            result_value = minvalue(result(board, action), v)
            if result_value > v:
                v = result_value
                best_action = action
    
    else:
        v = math.inf
        for action in action_set:
            result_value = maxvalue(result(board, action), v)
            if result_value < v:
                v = result_value
                best_action = action
    
    return best_action

def maxvalue(board, best_value):
    v = -math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, minvalue(result(board, action), v))
        if v > best_value:
          return v
    
    return v


def minvalue(board, best_value):
    v = math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, maxvalue(result(board, action), v))
        if v < best_value:
          return v

    return v