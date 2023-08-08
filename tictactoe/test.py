# Define a 2D list (list of lists) for Tic-Tac-Toe
board = [
    ['X', 'O', 'O'],
    ['None', 'X', 'O'],
    ['X', 'None', 'X']
]

# Determine whose turn it is
def get_next_player(board):
    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)
    
    if count_x == count_o:
        return 'X'
    elif count_x == count_o + 1:
        return 'O'
    else:
        return None

# Get the next player's turn
next_player = get_next_player(board)

# Print the result
if next_player:
    print(f"It's {next_player}'s turn.")
else:
    print("Invalid board state.")
