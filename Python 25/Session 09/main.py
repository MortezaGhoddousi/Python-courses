# # Example 1

# scores = input("Enter your scores splitted by ',': ")

# scores = scores.split(',')

# scores = [eval(s) for s in scores]

# Sum = 0

# for s in scores:
#     print(s**2)
#     Sum = Sum + s
    
# print(Sum / len(scores))

# print("end")

# import numpy

# print(numpy.average(scores))

# # Example 2

scores = input("Enter your scores splitted by ',': ")

scores = scores.split(',')

x = [eval(s) for s in scores]

# Min = 21
# Max = -1

# for i in x:
#     if i<Min:
#         Min = i
#     if i>Max:
#         Max = i

# print(Min, Max)

import numpy

print(numpy.min(x), numpy.max(x))




    
