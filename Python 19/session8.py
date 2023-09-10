import numpy as np
import random

def check_equal(a, b):
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

def find_states(states, envi):
    i = check_equal(states, np.reshape(envi, [1, np.size(envi)]))
    return i

dim = 3
actions = range(9)
states = np.zeros([1, dim*dim], dtype=int)
alpha = 0.01
gamma = 0.95

Q = np.zeros([1, len(actions)], dtype=float)

envi = np.zeros([1, dim*dim], dtype=int)

# num_state = find_states(states, envi)
# print(num_state)

# if (num_state == -1):
#     states = np.append(states, envi, axis=0)
#     Q = np.append(Q, np.zeros([1, len(actions)], dtype=float), axis=0)

# print(states)

a = random.choice(actions)
envi[0][a] = 1
r = 0
# print(envi)
snew = find_states(states, envi)
if (snew == -1):
    states = np.append(states, envi, axis=0)
    Q = np.append(Q, np.zeros([1, len(actions)], dtype=float), axis=0)

Q[0][a] = Q[0][a]+alpha*(r+gamma*np.max(Q[snew]))
print(Q)