import numpy as np

def hardlim (n):
    if n >= 0:
        return 1
    else:
        return 0

alpha = 0.1

P1 = np.array([[0], 
               [1]])
t1 = 1

P2 = np.array([[1], 
               [0]])
t2 = 0

W = np.array([[0, 0]])
b = 0


for i in range(5):
    n = np.matmul(W, P1) + b
    a = hardlim(n)

    e = t1 - a
    print(e, i)

    W = W + alpha*e*P1.transpose()
    b = b + alpha*e

    n = np.matmul(W, P2) + b
    a = hardlim(n)

    e = t2 - a

    W = W + alpha*e*P2.transpose()
    b = b + alpha*e
    print(e, i)

print(W)
print(b)
    

n = np.matmul(W, P1) + b
a = hardlim(n)
print(a, t1)

n = np.matmul(W, P2) + b
a = hardlim(n)
print(a, t2)

P3 = np.array([[0.1], 
               [0.9]])

n = np.matmul(W, P3) + b
a = hardlim(n)
print(a)

P4 = np.array([[0.8], 
               [0.2]])

n = np.matmul(W, P4) + b
a = hardlim(n)
print(a)


