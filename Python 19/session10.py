import numpy as np
import random
import pickle


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


with open('Q.pkl', 'rb') as f:
    Q = pickle.load(f)

with open('states.pkl', 'rb') as f:
    states = pickle.load(f)

print(states)
print(Q)
print(np.size(states, 0))

dim = 3
actions = range(9)
envi = np.zeros([1, dim*dim], dtype=int)

snew = find_states(states, envi)
print(snew)
a = np.argmax(Q[snew])
print(a)

envi[0][a] = 1
snew = find_states(states, envi)

s = snew
turn = True
MGh = True

while MGh:
    if turn:
        print(envi)
        ch = int(input("Your turn: "))
        if envi[0][ch] == 0:
            envi[0][ch] = 2

        snew = find_states(states, envi)
        
        if check_win(envi):
            MGh = False
        else: 
            if np.all(envi):
                MGh = False
        turn = False
    else:  
        a = np.argmax(Q[snew])
        print(Q[snew])
        print(snew)
        print(f"AI action is: {a}")
        if envi[0][a] == 0:
            envi[0][a] = 1
        else:
            while True:
                a = random.choice(actions)
                if envi[0][a] == 0:
                    envi[0][a] = 1
                    print(f"AI action is: {a}")
                    break

        snew = find_states(states, envi)      

        if check_win(envi):  
            MGh = False
        else: 
            if np.all(envi):
                MGh = False
            else:
                pass
                    
        s = snew
        turn = True

print(envi)