# # Exercise 1
# import numpy as np

# def poly (a:float, b:float, c:float) -> list:
#     delta = b**2 - 4*a*c
#     if delta > 0:
#         x1 = (-b + delta**0.5)/(2*a)
#         x2 = (-b - delta**0.5)/(2*a)
#         return [x1, x2]
#     elif delta == 0:
#         x = -b/(2*a)
#         return [x]
#     else:
#         x = 'no root'
#         return [x]
    
# print(poly(1, 3, 1))

# Exercise 2

import random

def showEnv(showMap:bool, env:list) -> None:
    envIndex = [["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]]
    
    if showMap:
        for row in envIndex:
            print(row)
    else:
        for row in env:
            print(row)

def findIndex(ind:str) -> list:
    envIndex = [["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]]    
    for row_index, row in enumerate(envIndex):
        for col_index, col in enumerate(row):
            if ind == col:
                return [row_index, col_index]
            
def Bot(env:list) -> list:
    Bot_row_index = random.randint(0, 2)
    Bot_col_index = random.randint(0, 2)

    while True:
        if env[Bot_row_index][Bot_col_index] == " ":
            return [Bot_row_index, Bot_col_index]
        else:
            Bot_row_index = random.randint(0, 2)
            Bot_col_index = random.randint(0, 2)


def checkWinner(env) -> bool:
    for i in range(3):
        if env[i][0] == env[i][1] and env[i][0] == env[i][2] and env[i][0] != " ":
            return True
        if env[0][i] == env[1][i] and env[0][i] == env[2][i] and env[0][i] != " ":
            return True
        
    if env[0][0] == env[1][1] and env[0][0] == env[2][2] and env[0][0] != " ":
            return True
    if env[0][2] == env[1][1] and env[0][2] == env[2][0] and env[0][2] != " ":
            return True
    return False
        




env = [[" ", " ", " "],
       [" ", " ", " "],
       [" ", " ", " "]]

turn = 0
while True:
    showEnv(True, env)
    print("="*30)
    player = input('enter your choose: ')
    [player_row_index, player_col_index] = findIndex(player)
    turn = turn +1

    env[player_row_index][player_col_index] = 'X'
    if checkWinner(env):
        print("player won")
        break

    if turn > 8:
        break
    print(f"player chose {player_row_index, player_col_index}")
    showEnv(False, env)
    print("="*30)

    [Bot_row_index, Bot_col_index] = Bot(env)
    env[Bot_row_index][Bot_col_index] = 'O'
    turn = turn +1
    if checkWinner(env):
        print("bot won")
        break

    if turn > 8:
        break
    print(f"bot chose {Bot_row_index, Bot_col_index}")
    showEnv(False, env)
    print("="*30)

    
showEnv(False, env)
print("="*30)
