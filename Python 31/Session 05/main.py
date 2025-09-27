# import random

def show_env(env):
    for row in env:
        print(row)

def find_index(env_index, player):
    for i in range(3):
        for j in range(3):
            if env_index[i][j] == player:
                return (i, j)
            
    return (None, None)

def check_winner(env, player):
    if env[0][0] == env[1][1] == env[2][2] and env[0][0] == player:
        return True
    elif env[0][2] == env[1][1] == env[2][0] and env[1][1] == player:
        return True   
    for i in range(3):
        if env[i][0] == env[i][1] == env[i][2] and env[i][0] == player:
            return True
        if env[0][i] == env[1][i] == env[2][i] and env[0][i] == player:
            return True
    return False


def check_draw(env):
    for i in range(3):
        for j in range(3):
            if env[i][j] == "_":
                return False
    return True


env = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
    ]

env_index = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
    ]


while True:
    print("*"*100)
    show_env(env_index)

    player1 = input('enter your choice: ')
    (player1_row, player1_column) = find_index(env_index, player1)
    while player1_row == None:
        player1 = input('enter your choice again: ')
        (player1_row, player1_column) = find_index(env_index, player1)

    env[player1_row][player1_column] = 'X'
    show_env(env)
    if check_winner(env, 'X'):
        print("player 1 won")
        break

    if check_draw(env):
        print("draw")
        break

    print("*"*100)
    show_env(env_index)

    player2 = input('enter your choice: ')
    (player2_row, player2_column) = find_index(env_index, player2)
    while player2_row == None:
        player2 = input('enter your choice again: ')
        (player2_row, player2_column) = find_index(env_index, player2)

    env[player2_row][player2_column] = 'O'
    show_env(env)

    if check_winner(env, 'O'):
        print("player 2 won")
        break

    if check_draw(env):
        print("draw")
        break


