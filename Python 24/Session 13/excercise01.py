import numpy as np

number = int(input('enter your number: '))

Sum = 0

for i in range(number):
    if ((np.mod(i, 3)==0) or (np.mod(i, 5)==0)):
        Sum = Sum + i
        
print(Sum)