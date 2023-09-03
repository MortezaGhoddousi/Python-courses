
# Tic-Tac_Toe 

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

# # 1: Player 1, 2: Player 2
# # Choosing who must start the game
# r = random.randint(1, 2)

# if r==1:
#     row = random.randint(0, 2)
#     col = random.randint(0, 2)
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
#     if nap:
#         row = random.randint(0, 2)
#         col = random.randint(0, 2)
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

# Removing empty strings in a list
check = True
li = ["Morteza", "Ali", "", "Nazanin", ""]
print(li)
while check:
    try:
        li.pop(li.index(""))
    except:
        check = False

print(li)


    




