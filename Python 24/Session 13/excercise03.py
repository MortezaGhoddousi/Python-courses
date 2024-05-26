import numpy as np

fibunacci = [1]
x = 0

while fibunacci[-1] < 4000000:
    fibunacci.append(x+fibunacci[-1])
    try:
        x = fibunacci[-2]
    except:
        x = fibunacci[-1]

    
fibunacci.pop(-1)  
print(fibunacci)

Sum = 0

for i in fibunacci:
    if (np.mod(i, 2)==0):
        Sum = Sum + i
        
        
print(Sum)

        