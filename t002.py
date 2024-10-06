import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 9)

# Check if there's a winner
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Check if the game is a draw
def check_draw(board):
    return all([spot != " " for row in board for spot in row])

# Get available spots
def get_available_spots(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax with alpha-beta pruning and depth limit for better AI behavior
def minimax(board, depth, is_maximizing, alpha, beta, depth_limit=6):
    if check_winner(board, 'O'):
        return 10 - depth  # AI wins
    if check_winner(board, 'X'):
        return depth - 10  # Human wins
    if check_draw(board) or depth >= depth_limit:  # Depth limit for complexity control
        return 0  # Draw or depth limit reached

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for (i, j) in get_available_spots(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta, depth_limit)
            board[i][j] = " "
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # Pruning
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for (i, j) in get_available_spots(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta, depth_limit)
            board[i][j] = " "
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  # Pruning
        return best_score

# AI move based on minimax with a dynamic depth limit
def ai_move(board, depth_limit=6):
    best_move = None
    best_score = -math.inf
    for (i, j) in get_available_spots(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf, depth_limit)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

# Function to give a hint (suggest best move for human)
def give_hint(board, depth_limit=6):
    best_move = None
    best_score = -math.inf
    for (i, j) in get_available_spots(board):
        board[i][j] = 'X'  # Assume human plays here
        score = minimax(board, 0, True, -math.inf, math.inf, depth_limit)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Human move with improved input validation
def human_move(board):
    while True:
        move = input("Enter your move (row and column separated by space, or type 'hint' for a suggestion): ")
        if move.lower() == "hint":
            hint = give_hint(board)
            if hint:
                print(f"Hint: You should move to row {hint[0]} and column {hint[1]}")
            else:
                print("No available hints. The board is full or game is over.")
            continue

        try:
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = 'X'
                break
            else:
                print("That spot is already taken. Try another.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column as numbers between 0 and 2.")

# Main game loop with AI move strategy
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'. You start first.")

    print_board(board)

    while True:
        # Human move
        human_move(board)
        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI move with dynamic depth strategy
        ai_move(board, depth_limit=6)
        print("AI has made its move:")
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
