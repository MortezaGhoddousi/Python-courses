# # Exercise 1
# import numpy as np
# import matplotlib.pyplot as plt

# # Create an array of x values from 0 to 2*pi
# x = np.linspace(0, 2*np.pi, 100)

# # Compute the corresponding y values using the cos function
# y = np.cos(3 * x)

# # Plot the function
# plt.plot(x, y)

# # Add labels and title
# plt.xlabel('x')
# plt.ylabel('cos(3x)')
# plt.title('Plot of cos(3x)')

# # Display the plot
# plt.show()

# Exercise 2

A = [[3,5,9],
     [1,0,2],
     [0,0,-1]]

B =[[1,2,3],
    [9,5,-3],
    [2,-1,7]]

# for row in A:
#     for cell in row:
#         print(cell)

X = []
for i in range(len(A)):
    row = []
    for j in range(len(A)):
        row.append(A[i][j]+B[i][j])
    X.append(row)
    
print(X)

Y = []

for i in range(len(A)):
    x = A[i]
    row = []
    for u in range(len(A)):
        y = []
        for j in range(len(A)):
            y.append(B[j][u])
        sum1 = 0
        for k in range(len(x)):
            sum1 = sum1 + x[k]*y[k]
        row.append(sum1)
    Y.append(row)
print(Y)

import numpy as np


A1 = np.array([[3, 5, 9], [1, 0, 2], [0, 0, -1]], dtype=int)
print(A1)
print(A1[2][2])

result = np.dot(A, B)

print(result)
