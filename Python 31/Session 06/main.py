# Example 1
# a = float(input("enter a: "))
# b = float(input("enter b: "))
# c = float(input("enter c: "))

# if a>b:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b>c:
#         print(b)
#     else:
#         print(c)

# print("end")

# Example 2
# score = 85

# if score >= 90:
#     print("Grade A")

# if score >= 80:
#     print("Grade B")

# if score >= 70:
#     print("Grade C")

# if score >= 60:
#     print("Grade D")

# print("end")

# Example 3
# import numpy as np
# r = float(input("Enter circle radius: "))
# A = np.pi * r**2

# print(A)

# Example 4
# i = 1
# while i<=10:
#     print(i)
#     j = i+1
#     while j<=10:
#         print(j)
#         j = j+1
#     i = i+1

# print("end")

# Example 5
# i = 0
# Sum = 0

# while i<3:
#     x = int(input("enter x: "))
#     Sum = x + Sum
#     i = i+1

# avg = Sum/i
# print(avg)

# Example 6
# N = int(input("enter N: "))
# M = 1
# F = 1
# while M != N:
#     M = M+1
#     F = F*M
# print(F)

# Example 7
import numpy as np

# block 1
Max = -1 * np.inf

# block 2
i = 0

while i<5: # block 3

    x = float(input("enter your number: ")) # block 4

    if x>Max: # block 5
        
        Max = x # block 6
    
    i = i+1 # block 7

# block 8
print(Max)
