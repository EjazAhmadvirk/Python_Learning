# Tic Tac Toe game in Python

# Function to print the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Input move
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid position! Please enter between 0 and 2.")
            continue
        if board[row][col] != " ":
            print("Cell already taken! Choose another one.")
            continue

        # Make move
        board[row][col] = current_player

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
