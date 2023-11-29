# import numpy as np
from numpy import array, zeros, where
from Functions import checkWin
import random

envi = zeros([3, 3], dtype=int)
indices = array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], dtype=int)          

turn = True
check = True

while check:
    if where(envi==0)[0].size == 0:
        print("Draw")
        check =False

    if turn:
        player = int(input("Enter your choice: "))
        turn = False
        row, column = where(indices==player)[0][0], where(indices==player)[1][0]

        envi[row][column] = 1
        winner = checkWin(envi)
        if not winner:
            pass
        else:
            print(winner)
            check = False

        print(envi)
    else:
        checkTrue = True
        while checkTrue:
            player = random.choice(indices)
            player = random.choice(player)
            row, column = where(indices==player)[0][0], where(indices==player)[1][0]
            if envi[row][column] == 0:
                envi[row][column] = 2
                checkTrue = False
                turn = True

        
        winner = checkWin(envi)
        if not winner:
            pass
        else:
            print(winner)
            check = False

        print(envi)






