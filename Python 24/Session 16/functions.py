import random

def show_env(env):
    for i in range(3):  
        print(env[i])

def update_env(env, user, check):
    if check:
        if env[int(user[0])-1][int(user[1])-1] == ' ':
            env[int(user[0])-1][int(user[1])-1] = 'X'
            return False, env
        else:
            print('wrong input, choose again ')
            return True, env
    else:
        if env[int(user[0])-1][int(user[1])-1] == ' ':
            env[int(user[0])-1][int(user[1])-1] = 'O'
            return False, env
        else:
            print('wrong input, choose again ')
            return True, env
            
            
def bot_choice():
    bot = [0, 0]
    bot[0] = random.randint(0, 2)
    bot[1] = random.randint(0, 2)
    return bot

def check_win(env):
    for i in range(3):
        if env[i][0] == env[i][1] and env[i][0] == env[i][2] and env[i][0] == 'X':
            return True, 0
        elif env[0][i] == env[1][i] and env[0][i] == env[2][i] and env[0][i] == 'X':
            return True, 0
        if env[i][0] == env[i][1] and env[i][0] == env[i][2] and env[i][0] == 'O':
            return True, 1
        elif env[0][i] == env[1][i] and env[0][i] == env[2][i] and env[0][i] == 'O':
            return True, 1
        
    if env[0][0] == env[1][1] and env[0][0] == env[2][2] and env[0][0] == 'X':
        return True, 0
    if env[0][2] == env[1][1] and env[0][2] == env[2][0] and env[0][2] == 'X':
        return True, 0
    if env[0][0] == env[1][1] and env[0][0] == env[2][2] and env[0][0] == 'O':
        return True, 1
    if env[0][2] == env[1][1] and env[0][2] == env[2][0] and env[0][2] == 'O':
        return True, 1
    return False, 2
            