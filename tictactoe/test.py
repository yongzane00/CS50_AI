# Define a sample Tic-Tac-Toe board
board = [
    ['None', 'None', 'None'],
    ['None', 'None', 'None'],
    ['None', 'None', 'None']
]

# Define constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define a function to check for a winning pattern (row, column, or diagonal)
def check_for_winner(board):
    # Check rows
    for row in board:
        if all(cell == PLAYER_X for cell in row):
            return PLAYER_X
        elif all(cell == PLAYER_O for cell in row):
            return PLAYER_O

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == PLAYER_X for row in range(len(board))):
            return PLAYER_X
        elif all(board[row][col] == PLAYER_O for row in range(len(board))):
            return PLAYER_O

    # Check diagonals
    if all(board[i][i] == PLAYER_X for i in range(len(board))):
        return PLAYER_X
    if all(board[i][len(board) - i - 1] == PLAYER_X for i in range(len(board))):
        return PLAYER_X
    if all(board[i][i] == PLAYER_O for i in range(len(board))):
        return PLAYER_O
    if all(board[i][len(board) - i - 1] == PLAYER_O for i in range(len(board))):
        return PLAYER_O

    return None  # No winner

# Define a function to check if the game is over
def game_over(board):
    # Check for a winning pattern or a full board
    if check_for_winner(board) is not None:
        return True
    return all(cell != 'None' for row in board for cell in row)

# Check if the game is over
if game_over(board):
    print("Game is over.")
else:
    print("Game is still ongoing.")
