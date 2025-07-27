# Exercise2
environment = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]

def findIndex(number):
    Index = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    for row in range(3):
        for column in range(3):
            if Index[row][column] == number:
                return (row, column)
            
def showEnv(environment):
    for row in environment:
        print(row)

def checkWinner(envi):
    for i in range(3):
        if envi[i][0] == envi[i][1] and envi[i][0] == envi[i][2] and envi[i][0] == "X":
            print("Player1 won")     
        if envi[0][i] == envi[1][i] and envi[0][i] == envi[2][i] and envi[0][i] == "X":
            print("Player1 won")
        if envi[i][0] == envi[i][1] and envi[i][0] == envi[i][2] and envi[i][0] == "O":
            print("Player2 won")     
        if envi[0][i] == envi[1][i] and envi[0][i] == envi[2][i] and envi[0][i] == "O":
            print("Player2 won")
    if envi[0][0] == envi[1][1] and envi[0][0] == envi[2][2] and envi[0][0] == "X":
        print("Player1 won")
    if envi[0][2] == envi[1][1] and envi[0][2] == envi[2][0] and envi[0][2] == "X":
        print("Player1 won")
    if envi[0][0] == envi[1][1] and envi[0][0] == envi[2][2] and envi[0][0] == "O":
        print("Player2 won")
    if envi[0][2] == envi[1][1] and envi[0][2] == envi[2][0] and envi[0][2] == "O":
        print("Player2 won")



showEnv(environment)    
while True:
    while True:
        player1 = int(input("Player1 -> Enter your choice in range of 1-9: "))
        (x, y) = findIndex(player1)
        if environment[x][y] == " ":
            environment[x][y] = "X"
            break
        else:
            print("You should choose an empty cell!")
    showEnv(environment)
    checkWinner(environment)

    while True:
        player2 = int(input("Player2 -> Enter your choice in range of 1-9: "))
        (x, y) = findIndex(player2)
        if environment[x][y] == " ":
            environment[x][y] = "O"
            break
        else:
            print("You should choose an empty cell!")
    showEnv(environment)
    checkWinner(environment)

