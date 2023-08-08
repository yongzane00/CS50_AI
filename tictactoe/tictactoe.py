"""
Tic Tac Toe Player
"""

import math

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

    # Not sure if i need to put any return here

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    none_positions = []
    if not terminal(board):
        # Find positions of all occurrences of 'None'
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'None':
                    none_positions.append((row, col))

    return none_positions   # This will return all tuple (i,j) which are equal to None

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if all elements in a row, column, or diagonal have the same symbol ('X' or 'O')
    def check_winner(elements):
        return all(element == elements[0] for element in elements)

    # Check for a winning pattern (row, column, or diagonal)
    def check_for_winner():
        for i in range(len(board)):
            row = board[i]
            column = [board[j][i] for j in range(len(board))]
            main_diagonal = [board[j][j] for j in range(len(board))]
            secondary_diagonal = [board[j][len(board)-1-j] for j in range(len(board))]

            if check_winner(row):
                return row[0]
            if check_winner(column):
                return column[0]
            if check_winner(main_diagonal):
                return main_diagonal[0]
            if check_winner(secondary_diagonal):
                return secondary_diagonal[0]
        return None
    
    winner_found = check_for_winner()

    if winner_found:
        return winner_found     # This will return either X or O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # print(board) = [[None, None, None], [None, None, None], [None, None, None]]
    # print(len(board)) = 3
    # print(type(board)) = <class 'list'>

    # Check if there's no 'None' in the board or if there's a winner
    def game_over(board):
        none_positions = any(cell == 'None' for row in board for cell in row)
        winner_found = winner(board)
        return not none_positions or winner_found is not None
    
    if game_over(board):
        return True
        
    return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Determine the game result
    def get_game_result(board):
        winner_found = winner(board)
        if winner_found == 'X':
            return 1
        elif winner_found == 'O':
            return -1
        else:
            return 0

    # Get the game result
    utility_score = get_game_result(board)
    return utility_score
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
