def checkWinner(env):
    for j in range(3):
        if env[j][0] == env[j][1] == env[j][2] and env[j][0] != "_":
            return True
        if env[0][j] == env[1][j] == env[2][j] and env[0][j] != "_":
            return True
            
    if env[0][0] == env[1][1] == env[2][2] and env[0][0] != "_":
        return True
        
    if env[0][2] == env[1][1] == env[2][0] and env[0][2] != "_":
        return True
    
    return False

def showEnv(env):
    for i in env:
        print(i)

def change2Int(player):
    p = []
    for i in player:
        p.append(int(i))
    # p1 = [int(i) for i in player1]
    return p

env = [["_", "_", "_"],
       ["_", "_", "_"],
       ["_", "_", "_"]]

showEnv(env)

while True:
    player1 = input("Enter your choice: ").split(" ")

    p1 = change2Int(player1)

    env[p1[0]][p1[1]] = "X"
    if checkWinner(env):
        showEnv(env)
        print("Player 1 won")
        break
    
    showEnv(env)

    player2 = input("Enter your choice: ").split(" ")

    p2 = change2Int(player2)

    env[p2[0]][p2[1]] = "O"

    if checkWinner(env):
        showEnv(env)
        print("Player 2 won")
        break

    showEnv(env)



# st = "Mortza ghoddousi 32"
# splitted_string = st.split(" ")
# print(splitted_string)




