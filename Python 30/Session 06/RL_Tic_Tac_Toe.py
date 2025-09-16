import random
import numpy as np
import pickle

# Helper function: Check if player has won
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

# Check if board state is valid (used to generate all states)
def is_valid_state(board):
    count_X = board.count('X')
    count_O = board.count('O')
    
    if count_O > count_X or count_X - count_O > 1:
        return False
    if has_won(board, 'X') and has_won(board, 'O'):
        return False
    if has_won(board, 'X') and count_X != count_O + 1:
        return False
    if has_won(board, 'O') and count_X != count_O:
        return False
    return True

# Generate all valid states for indexing
states = []
def generate_all_states(board=['_']*9, index=0):
    if index == 9:
        if is_valid_state(board):
            states.append(board.copy())
        return
    for mark in ['_', 'X', 'O']:
        board[index] = mark
        generate_all_states(board, index + 1)

generate_all_states()

# Convert board to state index in states list
def board_to_index(board):
    for i, state in enumerate(states):
        if state == board:
            return i
    return None  # Not found (shouldn't happen if states are correct)

# Random bot (Bot2)
def Bot(env:list) -> list:
    empty_cells = [i for i, cell in enumerate(env) if cell == '_']
    return [random.choice(empty_cells)] if empty_cells else []

# Epsilon-greedy selection on Q-values for current state
def epsilon_greedy(q_values, epsilon):
    if random.random() < epsilon:
        return random.randint(0, len(q_values) - 1)
    else:
        max_q = max(q_values)
        best_actions = [i for i, q in enumerate(q_values) if q == max_q]
        return random.choice(best_actions)

# Parameters
actions = list(range(9))  # 9 possible moves (cells 0-8)
Q_table = np.zeros((len(states), len(actions)))  # Q-values table
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

num_episodes = 100000

for episode in range(num_episodes):
    state = ['_'] * 9  # Reset board
    done = False
    turn = 0
    
    while not done:
        # Get current state index
        state_idx = board_to_index(state)
        if state_idx is None:
            break  # Invalid state
        
        # Bot1's turn (learning agent)
        q_values = Q_table[state_idx]
        action = epsilon_greedy(q_values, epsilon)
        
        # If chosen action cell is occupied, choose random valid cell instead (to avoid errors)
        if state[action] != '_':
            empty_cells = [i for i, c in enumerate(state) if c == '_']
            if not empty_cells:
                done = True
                reward = 0  # Draw
                break
            action = random.choice(empty_cells)
        
        # Make move for Bot1 (X)
        state[action] = 'X'
        turn += 1
        
        # Check if Bot1 won
        if has_won(state, 'X'):
            reward = 10
            done = True
            # Update Q-value for last action with reward (terminal)
            Q_table[state_idx, action] += alpha * (reward - Q_table[state_idx, action])
            break
        
        # Check for draw
        if turn >= 9 or all(c != '_' for c in state):
            reward = -1  # Draw reward
            done = True
            # Update Q-table
            Q_table[state_idx, action] += alpha * (reward - Q_table[state_idx, action])
            break
        
        # Bot2's turn (random bot O)
        [bot2_action] = Bot(state)
        state[bot2_action] = 'O'
        turn += 1
        
        # Check if Bot2 won
        if has_won(state, 'O'):
            reward = -10
            done = True
            # Update Q-value for Bot1's last action with negative reward
            Q_table[state_idx, action] += alpha * (reward - Q_table[state_idx, action])
            break
        
        # Otherwise, reward is 0 (game continues)
        reward = 0
        
        # Get next state index
        next_state_idx = board_to_index(state)
        if next_state_idx is None:
            done = True
            break
        
        # Q-learning update for Bot1's last action
        max_next_q = max(Q_table[next_state_idx])
        Q_table[state_idx, action] += alpha * (reward + gamma * max_next_q - Q_table[state_idx, action])

print("Training complete!")

# Save Q_table and states for later use
with open('tic_tac_toe_agent.pkl', 'wb') as f:
    pickle.dump({'Q_table': Q_table, 'states': states}, f)
print("Agent data saved to 'tic_tac_toe_agent.pkl'")

# Example: play one game with trained Bot1 (greedy)
state = ['_'] * 9
done = False
turn = 0

while not done:
    state_idx = board_to_index(state)
    if state_idx is None:
        break
    
    # Bot1 action: greedy (epsilon=0)
    q_values = Q_table[state_idx]
    action = epsilon_greedy(q_values, epsilon=0.0)
    
    if state[action] != '_':
        empty_cells = [i for i, c in enumerate(state) if c == '_']
        if not empty_cells:
            print("Draw!")
            break
        action = random.choice(empty_cells)
    
    state[action] = 'X'
    turn += 1
    
    print("Bot1 (X) plays:", action)
    print("Board:", state)
    
    if has_won(state, 'X'):
        print("Bot1 wins!")
        break
    
    if turn >= 9 or all(c != '_' for c in state):
        print("Draw!")
        break
    
    [bot2_action] = Bot(state)
    state[bot2_action] = 'O'
    turn += 1
    print("Bot2 (O) plays:", bot2_action)
    print("Board:", state)
    
    if has_won(state, 'O'):
        print("Bot2 wins!")
        break
