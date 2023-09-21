import numpy as np

def activationFunction(n):
    if n >= 0:
        return 1
    else:
        return 0

# p1 = np.array([[1, 2]], dtype=float)
# t1 = 1

# p2 = np.array([[-1, 2]], dtype=float)
# t2 = 0

# p3 = np.array([[0, -1]], dtype=float)
# t3 = 0

p = np.array([[1, 2],
               [-1, 2],
               [0, -1]], dtype=float)

t = np.array([1, 0, 0], dtype=int)

w = np.array([0, 0], dtype=float)
b = np.array([0], dtype=float)


# Train the Network
for iter in range(10):
    for i in range(3):
        n = np.matmul(w, p[i].T) + b
        a = activationFunction(n)

        e = t[i]-a
        w = w + e*p[i]
        b = b + e

print(w, b)

# Test the network
p1 = np.array([[2, 2]], dtype=float)
n = np.matmul(w, p1.T) + b
print(n)
a = activationFunction(n)
print(a)

