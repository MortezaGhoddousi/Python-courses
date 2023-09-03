# # Tic-Tac_Toe 

# import numpy as np
# import random

# # Define Stop criterion
# def check(envi):
#     for j in range(1, 3):
#         for i in range(3):
#             if envi[i][0] == envi[i][1] and envi[i][0] == envi[i][2] and envi[i][0] == j:
#                 print(f"Player {j} won")
#                 return True
#         for i in range(3):
#             if envi[0][i] == envi[1][i] and envi[0][i] == envi[2][i] and envi[0][i] == j:
#                 print(f"Player {j} won")
#                 return True
#         if envi[0][0] == envi[1][1] and envi[0][0] == envi[2][2] and envi[0][0] == j:
#             print(f"Player {j} won")
#             return True
#         if envi[0][2] == envi[1][1] and envi[0][2] == envi[2][0] and envi[0][2] == j:
#             print(f"Player {j} won")
#             return True
    
#     return False

# # Making the environment of Tic Tac Toe
# dim = 3
# envi = np.zeros([dim, dim], dtype=int)

# # 1: Player 1, 2: Bot
# # Choosing who must start the game
# r = random.randint(1, 2)

# if r==1:
#     row = int(input("Enter your choice: (0:2 your row choice)"))
#     col = int(input("Enter your choice: (0:2 your column choice)"))
#     envi[row][col] = 1
#     nap = False
# elif r==2:
#     row = random.randint(0, 2)
#     col = random.randint(0, 2)
#     envi[row][col] = 2
#     nap = True

# # Main Loop
# stopcon = True
# counter = 0
# while stopcon:
#     print(envi)
#     if nap:
#         row = int(input("Enter your choice: (0:2 your row choice)"))
#         col = int(input("Enter your choice: (0:2 your column choice)"))
#         if envi[row][col] == 0:
#             envi[row][col] = 1
#             nap = False
#     else:
#         row = random.randint(0, 2)
#         col = random.randint(0, 2)
#         if envi[row][col] == 0:
#             envi[row][col] = 2
#             nap = True    
#     stopcon = not check(envi)
#     counter = counter+1
#     if counter > 100:
#         print("Draw")
#         stopcon = False

# print(envi)


# Perceptron Network

import numpy as np

#Defining Activation Function
def activation_function(n):
    if n >= 0:
        return 1
    else:
        return -1

# Initialize
apple = np.array([0, 1, 0], dtype=float)[np.newaxis] # d = 1
cucumber = np.array([1, 0, 1], dtype=float)[np.newaxis] # d = -1

p1 = np.array([.7, .1, .82])[np.newaxis]

w = np.zeros([1, 3], dtype=float)
b = np.zeros([1, 1], dtype=float)

r = 0.1

# FeedForward
for i in range(10000):
    P = apple.T
    n = np.matmul(w, P) + b
    a = activation_function(n)

    w = w + r*(1 - a)*P.T
    b = b + r*(1- a)

    P = cucumber.T
    n = np.matmul(w, P) + b
    a = activation_function(n)

    w = w + r*(-1 - a)*P.T
    b = b + r*(-1 - a)

print(w)

# Testion the network
P = p1.T
n = np.matmul(w, P) + b
a = activation_function(n)

print(a)

p2 = np.array([.2, .8, .1])[np.newaxis]
P = p2.T
n = np.matmul(w, P) + b
a = activation_function(n)

print(a)









