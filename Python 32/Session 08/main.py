import numpy as np

p_apple = np.array([[1],
                    [1],
                    [0]])

t_apple = 1

p_cucumber = np.array([[0],
                       [0],
                       [1]])

t_cucumber = 0

w = np.array([[0, 0, 0]])
b = 0

alpha = 0.1


for i in range(10):
    n = np.matmul(w, p_apple) + b

    if n >= 0:
        a = 1
    else:
        a = 0

    e = t_apple-a

    w = w+alpha*e*np.transpose(p_apple)
    b = b+alpha*e

    n = np.matmul(w, p_cucumber) + b

    if n >= 0:
        a = 1
    else:
        a = 0

    e = t_cucumber-a

    w = w+alpha*e*np.transpose(p_cucumber)
    b = b+alpha*e


p_test_apple = [0.85, 0.75, 0.15]
n = np.matmul(w, p_test_apple) + b

if n >= 0:
    a = "apple"
else:
    a = "cucumber"

print(p_test_apple,a)

p_test_cucumber = [0.1, 0.2, 0.9]
n = np.matmul(w, p_test_cucumber) + b

if n >= 0:
    a = "apple"
else:
    a = "cucumber"

print(p_test_cucumber,a)













































