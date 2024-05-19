import numpy as np

def octal(x):
    x1 = np.zeros([1, 4], dtype=int)

    i = 0
    while x != 0:
        x1 [0][i] = np.mod(x, 8)
        x = x//8
        i = i+1
    
    
    x2 = ''  
    for i in range(3, -1, -1):
        x2 = x2 + str(x1[0][i])
    return x2


def hexa(x):
    
    x1 = np.zeros([1, 4], dtype=str)

    i = 0
    while x != 0:
        x3 = np.mod(x, 16)
        if x3 == 10:
            x3 = 'a'
        elif x3 == 11:
            x3 = 'b'
        elif x3 == 12:
            x3 = 'c'
        elif x3 == 13:
            x3 = 'd'
        elif x3 == 14:
            x3 = 'e'
        elif x3 == 15:
            x3 = 'f'
        
        x1 [0][i] = x3
        
        x = x//16
        i = i+1
    
    
    x2 = ''  
    for i in range(3, -1, -1):
        x2 = x2 + str(x1[0][i])
    return x2
    
