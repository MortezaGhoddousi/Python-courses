import numpy as np


def hardlim(n):
    if n >= 0:
        return 1
    else:
        return 0


alpha = 0.1

P_rect = np.array([[0],
                   [1]])

P_circle = np.array([[1],
                     [0]])

T_rect = 1
T_circle = 0

W = np.array([[0, 0]])
b = 0

for i in range(5):
    P = P_rect

    n = np.matmul(W, P) + b
    a = hardlim(n)

    e = T_rect - a

    W = W + alpha*(e*np.transpose(P))
    b = b + alpha*e

    P = P_circle

    n = np.matmul(W, P) + b
    a = hardlim(n)

    e = T_circle - a

    W = W + alpha*(e*np.transpose(P))
    b = b + alpha*e

print(W)
print(b)


P_test = np.array([[0.1],
                   [0.9]])

n = np.matmul(W, P_test) + b
a = hardlim(n)

print("input is Rectagle")
if a == 1:
    print("Rectangle")
else:
    print("Circle")

P_test = np.array([[0.87],
                   [0.2]])

n = np.matmul(W, P_test) + b
a = hardlim(n)

print("input is Circle")
if a == 1:
    print("Rectangle")
else:
    print("Circle")
print("end")





