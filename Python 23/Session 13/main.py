# # EX1 

# numStu = int(input('Please enter the number of your students: '))

# i = 0
# Sum = 0
# Min = 21
# Max = -1

# scores = []

# while i < numStu:
#     x = float(input(f"Enter the {i+1}th score: "))
#     scores.append(x)
#     print(scores)
#     Sum = Sum+x

#     if x < Min:
#         Min = x
    
#     if x > Max:
#         Max = x

#     i = i+1

# print(f"The average is: {Sum/numStu}")
# print(f"The minimum is: {Min}")
# print(f"The maximum is: {Max}")

import numpy

numStu = int(input('Please enter the number of your students: '))

i = 0
scores = []

while i < numStu:
    x = float(input(f"Enter the {i+1}th score: "))
    scores.append(x)
    i = i+1

print(scores)

print(f"The average is: {numpy.average(scores)}")
print(f"The minimum is: {numpy.amin(scores)}")
print(f"The maximum is: {numpy.amax(scores)}")

