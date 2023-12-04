# import numpy as np
from numpy import array, zeros, where, argmax
from Functions import checkWin, find_states
import random
import pickle

with open('Q.pkl', 'rb') as f:
    Q = pickle.load(f)
    
with open('states.pkl', 'rb') as f:
    states = pickle.load(f)


environment = zeros([3, 3], dtype=int)

envi = zeros([1, 9], dtype=int)

indices = array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], dtype=int)          

turn = True
check_win = True

while check_win:
    if where(envi==0)[0].size == 0:
        print("Draw")
        check_win =False

    elif turn:
        player = int(input("Enter your choice: "))
        envi[0][player-1] = 1
        turn = False
        row, column = where(indices==player)[0][0], where(indices==player)[1][0]

        environment[row][column] = 1
        Winner = checkWin(envi)
        if Winner: 
            print("Player won")
            check_win = False

        print(environment)
    else:
        checkTrue = True
        while checkTrue:
            # AIChoice = random.choice(indices)
            # AIChoice = random.choice(AIChoice)
            snew = find_states(states, envi)
            AIChoice = argmax(Q[snew])
            row, column = where(indices==AIChoice+1)[0][0], where(indices==AIChoice+1)[1][0]
            
            if envi[0][AIChoice] == 0:
                envi[0][AIChoice] = 2            
                environment[row][column] = 2
                checkTrue = False
                turn = True
            else:
                AIChoice = random.choice(indices)
                AIChoice = random.choice(AIChoice)
                print(AIChoice)
                row, column = where(indices==AIChoice)[0][0], where(indices==AIChoice)[1][0]               
                if envi[0][AIChoice] == 0:
                    envi[0][AIChoice] = 2            
                    environment[row][column] = 2
                    checkTrue = False
                    turn = True 

        
        Winner = checkWin(envi)
        if Winner: 
            print("AI won")
            check_win = False

        print(environment)

