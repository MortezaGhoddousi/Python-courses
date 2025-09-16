import pickle

# Load trained agent
with open('tic_tac_toe_agent.pkl', 'rb') as f:
    data = pickle.load(f)

Q_table = data['Q_table']
states = data['states']

# Functions (same as training script)
def has_won(board, player):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def board_to_index(board):
    for i, state in enumerate(states):
        if state == board:
            return i
    return None

def print_board(board):
    symbols = [c if c != '_' else ' ' for c in board]
    print(f"{symbols[0]} | {symbols[1]} | {symbols[2]}")
    print("--+---+--")
    print(f"{symbols[3]} | {symbols[4]} | {symbols[5]}")
    print("--+---+--")
    print(f"{symbols[6]} | {symbols[7]} | {symbols[8]}")

def epsilon_greedy(q_values, epsilon=0.0):
    # Greedy: epsilon=0 to always pick best action
    import random
    if random.random() < epsilon:
        return random.randint(0, len(q_values) - 1)
    else:
        max_q = max(q_values)
        best_actions = [i for i, q in enumerate(q_values) if q == max_q]
        return random.choice(best_actions)

def get_valid_moves(board):
    return [i for i, c in enumerate(board) if c == '_']

def human_move(board):
    valid = get_valid_moves(board)
    while True:
        try:
            move = int(input(f"Your turn! Choose a position {valid}: "))
            if move in valid:
                return move
            else:
                print(f"Invalid move! Choose from {valid}")
        except ValueError:
            print("Please enter a valid integer.")

def bot_move(board):
    state_idx = board_to_index(board)
    if state_idx is None:
        # Should not happen, fallback to random
        valid = get_valid_moves(board)
        return valid[0] if valid else None

    q_values = Q_table[state_idx]
    valid_moves = get_valid_moves(board)

    # Filter q_values to valid moves only
    valid_q_values = [(move, q_values[move]) for move in valid_moves]
    max_q = max(q for move, q in valid_q_values)
    best_moves = [move for move, q in valid_q_values if q == max_q]

    return best_moves[0]  # pick first best move

def main():
    board = ['_'] * 9
    print("Welcome to Tic-Tac-Toe! You play O, bot plays X and goes first.")
    print_board(board)

    while True:
        # Bot (X) move
        move = bot_move(board)
        if move is None:
            print("No valid moves left! It's a draw.")
            break
        board[move] = 'X'
        print(f"\nBot (X) plays: {move}")
        print_board(board)

        if has_won(board, 'X'):
            print("Bot (X) wins! Better luck next time.")
            break
        if '_' not in board:
            print("It's a draw!")
            break

        # Human (O) move
        move = human_move(board)
        board[move] = 'O'
        print_board(board)

        if has_won(board, 'O'):
            print("Congratulations! You won!")
            break
        if '_' not in board:
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
