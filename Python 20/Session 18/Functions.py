import numpy as np

def checkWin(envi):
    s1 = np.size(envi)
    s1 = int(np.sqrt(s1))
    for i in range(s1):
        if envi[0][i+0] == envi[0][i+3] and envi[0][i+0] == envi[0][i+6] and envi[0][i+0] != 0:
            return True
        if envi[0][3*i+0] == envi[0][3*i+1] and envi[0][3*i+0] == envi[0][3*i+2] and envi[0][3*i+0] != 0:
            return True
    if envi[0][0] == envi[0][4] and envi[0][0] == envi[0][8] and envi[0][0] != 0:
        return True
    if envi[0][2] == envi[0][4] and envi[0][0] == envi[0][6] and envi[0][2] != 0:
        return True
    return False

    
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

