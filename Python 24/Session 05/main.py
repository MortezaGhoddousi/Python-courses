# Example 2

# a = int(input("Enter your first number: "))
# b = input("Enter your second number: ")
# b = int(b)
# print(a/b)

# Example 3

# mylist = range(0, 11, 2)
# print(mylist)
# for i in mylist:
#     print(i)

# Sum = 0
# for i in range(101):
#     Sum = Sum + i
# print(Sum)

# Example 4

# for i in range(10):
#     for j in range(10):
#         print(f'{i} * {j} = {i*j}')

# Example 5
# mylist = [4, 2, 7, 8, 10, 15, 20, 4, 20, 19.5, 17]
# print(len(mylist))
# Sum = 0
# for i in mylist:
#     Sum = Sum + i
# print(Sum / len(mylist))

# import numpy as np
from numpy import var, average, amin

myList = [7, 4, 99, 64, 2]

Min = amin(myList)
print(Min)

print(var(myList))
print(average(myList))



