import numpy as np
import random
import pickle

# Define Function for finding state in states
# It will return number of state if it exists, O.W will return -1

def find_states(a, b):
    s1 = np.size(a, 0)
    s2 = np.size(a, 1)
    for i in range(s1):
        counter = 0
        for j in range(s2):
            if a[i][j] != b[0][j]:
                counter = counter+1
        if counter == 0:
            return i
    return -1

# Define Function in order to check if the game is finished or not

def check_win(envi):
    s1 = np.size(envi)
    s1 = int(np.sqrt(s1))
    for i in range(s1):
        if envi[0][i+0] == envi[0][i+3] and envi[0][0] == envi[0][i+6] and envi[0][i+0] != 0:
            return True
        if envi[0][3*i+0] == envi[0][3*i+1] and envi[0][0] == envi[0][3*i+2] and envi[0][3*i+0] != 0:
            return True
    if envi[0][0] == envi[0][4] and envi[0][0] == envi[0][8] and envi[0][0] != 0:
        return True
    if envi[0][2] == envi[0][4] and envi[0][0] == envi[0][6] and envi[0][2] != 0:
        return True
    return False


# Initialization
dim = 3
actions = range(9)
states = np.zeros([1, dim*dim], dtype=int)
alpha = 0.01
gamma = 0.95
max_it = 10000

# Q-table
Q = np.zeros([1, len(actions)], dtype=float)

# Main loop
for iter in range(max_it): 
    envi = np.zeros([1, dim*dim], dtype=int)
    a = random.choice(actions)
    envi[0][a] = 1
    r = 0

    snew = find_states(states, envi)
    # if new state does not exist in states, it will be created
    if (snew == -1):
        states = np.append(states, envi, axis=0)
        Q = np.append(Q, np.zeros([1, len(actions)], dtype=float), axis=0)

    # Updating Q-table
    Q[0][a] = Q[0][a]+alpha*(r+gamma*np.max(Q[snew]))

    s = snew
    turn = True

    MGh = True
    while MGh:
        if turn:
            acc = True
            while acc:
                ch = random.choice(actions)
                if envi[0][ch] == 0:
                    envi[0][ch] = 2
                    acc = False

            snew = find_states(states, envi)
            if (snew == -1):
                states = np.append(states, envi, axis=0)
                Q = np.append(Q, np.zeros([1, len(actions)], dtype=float), axis=0)
            if check_win(envi):
                MGh = False
            else: 
                if np.all(envi):
                    MGh = False
                else:
                    pass
            turn = False
        else:  
            a = random.choice(actions)
            if envi[0][a] == 0:
                envi[0][a] = 1
                r = 0
            else:
                MGh = False
                r = -5
    
            snew = find_states(states, envi)
            if (snew == -1):
                states = np.append(states, envi, axis=0)
                Q = np.append(Q, np.zeros([1, len(actions)], dtype=float), axis=0)

            if check_win(envi):
                r = 10   
                MGh = False
            else: 
                if np.all(envi):
                    MGh = False
                else:
                    pass
                       
            Q[s][a] = Q[s][a]+alpha*(r+gamma*np.max(Q[snew]))
            s = snew
            turn = True


with open('file.pkl', 'wb') as f:
    pickle.dump(Q, f)
            
print(Q)
print(envi)
print(states)
print(np.size(states, 0))
        