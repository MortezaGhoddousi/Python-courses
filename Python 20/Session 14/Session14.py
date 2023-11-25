import numpy as np

def activation_function(n):
    if n<0:
        a = -1
    else:
        a = 1
    return a

P1 = np.array([[1], [-1], [-1]], dtype=int) #Apple
P2 = np.array([[1], [1], [-1]], dtype=int) #Cucumber

t1 = -1 #Apple
t2 = 1 #Cucumber

W = np.random.rand(1, 3)
b = np.random.rand()

for i in range(100):
    if i%2 == 0:
        # n = W*P+b
        n = np.dot(W, P1) + b
        a = activation_function(n)
        e = t1-a
        W = W + (e*np.transpose(P1))
        b = b + e

    else:
        # n = W*P+b
        n = np.dot(W, P2) + b
        a = activation_function(n)
        e = t2-a
        W = W + (e*np.transpose(P2))
        b = b + e

print(W)
print(b)

Apple = np.array([[0.9], [-0.8], [-0.86]], dtype=float) #Apple
n = np.dot(W, Apple) + b
a = activation_function(n)

print(a)

Cucumber = np.array([[0.87], [0.8], [-0.7]], dtype=float) #Cucumber
n = np.dot(W, Cucumber) + b
a = activation_function(n)

print(a)






