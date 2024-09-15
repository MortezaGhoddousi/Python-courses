import numpy as np
import matplotlib.pyplot as plt

def hardlim (n):
    if n >= 0:
        return 1
    else:
        return 0

pApple = np.array([[1], 
                   [0], 
                   [0]])

pCucumber = np.array([[1], 
                   [1], 
                   [1]])

tApple = 1
tCucumber = 0

W = np.array([[0, 0, 0]])
b = 0

error = []

for i in range(10):
    # 1 
    n = np.matmul(W, pApple) + b
    a = hardlim(n)

    # 2
    e = tApple - a
    error.append(e)
    # 3
    W = W + e * np.transpose(pApple)
    b = b + e

    # 1 
    n = np.matmul(W, pCucumber) + b
    a = hardlim(n)

    # 2
    e = tCucumber - a
    error.append(e)
    # 3
    W = W + e * np.transpose(pCucumber)
    b = b + e
    
print(W, b)

n = np.matmul(W, pCucumber) + b
a = hardlim(n)

print(a)
if a == 1 :
    print('Apple')
else:
    print('Cucumber')
    
n = np.matmul(W, pApple) + b
a = hardlim(n)

print(a)
if a == 1 :
    print('Apple')
else:
    print('Cucumber')
    
p = np.array([[0.8], 
              [0.1], 
              [0.3]])

n = np.matmul(W, p) + b
print(n)
a = hardlim(n)
print(a)

if a == 1 :
    print('Apple')
else:
    print('Cucumber')
    
    
plt.figure()

plt.plot(error)
plt.title('Error')

plt.show()