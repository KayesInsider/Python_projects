def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves_left = 9

    while moves_left > 0:
        print_board(board)
        print(f"Player {current_player}'s turn")
        move = get_move()
        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = current_player
        moves_left -= 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        if moves_left == 0:
            print_board(board)
            print("It's a tie!")
            return

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
