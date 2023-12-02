from numpy import array, zeros, where, append
from numpy import max as Max
# import numpy as np
from Functions import checkWin, find_states
import random
import pickle



alpha = 0.1
gamma = 0.9
actions = range(1, 10)

envi = zeros([1, 9], dtype=int)

states = zeros([1, 9], dtype=int)
with open('Q.pkl', 'rb') as f:
    Q = pickle.load(f)
# Q = zeros([1, 9], dtype=int)

maxit = 5000


for iteration in range(maxit):
    envi = zeros([1, 9], dtype=int)
    
    print(iteration)
    
    check_win = True
    turn = True
    while check_win:
        if where(envi==0)[0].size == 0:
            # print("Draw")
            check_win = False
               
        elif turn:
            snew = find_states(states, envi)
            if (snew == -1):
                states = append(states, envi, axis=0)
                Q = append(Q, zeros([1, len(actions)], dtype=float), axis=0)
            checkTrue = True
            while checkTrue:
                a = random.choice(actions)
                if envi[0][a-1] == 0:
                        envi[0][a-1] = 1
                        checkTrue = False
                        turn = False       
                        r = -0.1
            Winner = checkWin(envi)
            if Winner: 
                r = 10
                check_win = False

            Q[snew][a-1] = Q[snew][a-1]+alpha*(r+gamma*Max(Q[snew]))
        else:
            snew = find_states(states, envi)
            if (snew == -1):
                states = append(states, envi, axis=0)
                Q = append(Q, zeros([1, len(actions)], dtype=float), axis=0)
            checkTrue = True
            while checkTrue:
                a = random.choice(actions)
                if envi[0][a-1] == 0:
                        envi[0][a-1] = 2
                        checkTrue = False
                        turn = True 
            Winner = checkWin(envi)
            if Winner: 
                check_win = False  
                r = -10
                Q[snew][a-1] = Q[snew][a-1]+alpha*(r+gamma*Max(Q[snew])) 


    snew = find_states(states, envi)
    if (snew == -1):
        states = append(states, envi, axis=0)
        Q = append(Q, zeros([1, len(actions)], dtype=float), axis=0)
    # print(envi)
    
with open('Q.pkl', 'wb') as f:
    pickle.dump(Q, f)
    
with open('states.pkl', 'wb') as f:
    pickle.dump(states, f)
    
    
print(states)
print(states.shape)
print(Q)
print(Q[0])








