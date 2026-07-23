# import numpy as np

# def hardlim(n):
#     a = []
#     for i in n[0]:
#         if i>=0:
#             a.append(1)
#         else:
#             a.append(0)
#     return a

# alpha = 0.1

# P = np.array([[1, 2, 1, 2, 3, -1, -2, -3],
#               [2, 1, 4, 3, 1, -1, -2, -1]])


# T = np.array([[1, 1, 1, 1, 1, 0, 0, 0]])

# W = np.random.randn(1, 2)
# b = np.random.randn(1, 8)

# for i in range(100):
#     n = np.matmul(W, P) + b
#     a = hardlim(n)
#     e = T-a
#     W = W + 2*alpha*(np.matmul(e, np.transpose(P)))
#     b = b + 2*alpha*e

    

# print(W)
# print(b)
# print("done")

# P_test = np.array([[0.5, -2, -1, 2, 3, -1, -1, 3],
#                    [2.5, -1, -4, 1, 1, -3, -4, 2]])

# n = np.matmul(W, P_test) + b
# a = hardlim(n)

# print(a)



prices = [16, 14.5, 17.4, 22, 14, 16.5, 20]

# < 15 => 0
# > 15 and < 16 => 10
# > 16 and <17 => 25
# > 17 and < 20 => 30
# > 20 => 45

tax = []
for p in prices:
    if p < 15:
        tax.append(p)
    elif p >= 15 and p < 16:
        tax.append(p*0.9)
    elif p >= 16 and p < 17:
        tax.append(p*0.75)
    elif p >= 17 and p < 20:
        tax.append(p*0.7)
    else:
        tax.append(p*0.55)

print(tax)




