"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

# This is 8Aug
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

    if board == initial_state():
        return X    # X start first
    
    elif not terminal(board):
        count_x = sum(row.count('X') for row in board)
        count_o = sum(row.count('O') for row in board)
        
        if count_x == count_o:
            return X    # X's turn
        elif count_x == count_o + 1:
            return O    # O's turn

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    none_positions = set()
    if not terminal(board):
        # Find positions of all occurrences of 'None'
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == EMPTY:
                    none_positions.add((row, col))

    return none_positions   # This will return all tuple (i,j) which represent all the possible actions

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Create new board, without modifying the original board received as input
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == X for row in range(len(board))):
            return X
        elif all(board[row][col] == O for row in range(len(board))):
            return O

    # Check diagonals
    if all(board[i][i] == X for i in range(len(board))):
        return X
    if all(board[i][len(board) - i - 1] == X for i in range(len(board))):
        return X
    if all(board[i][i] == O for i in range(len(board))):
        return O
    if all(board[i][len(board) - i - 1] == O for i in range(len(board))):
        return O

    return None  # No winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Define a function to check if the game is over
    def game_over(board):
        # Check for a winning pattern or a full board
        if winner(board) is not None:
            return True
        return all(cell != EMPTY for row in board for cell in row)

    # Check if the game is over
    if game_over(board):
        return True
    else:
        return False
    

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Determine the game result
    if terminal(board):
        winner_found = winner(board)
        if winner_found == X:
            return 1
        elif winner_found == O:
            return -1
        else:
            return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
