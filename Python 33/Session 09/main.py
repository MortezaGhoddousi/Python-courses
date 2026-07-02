# ex1

# n = 5
# i = 0
# s = 0
# numbers = []
# while i<n:
#     x = float(input("enter your number: "))
#     numbers.append(x)
#     s = s + x
#     i = i+1

# avg = s / n

# print(numbers)

# i = 0
# s = 0
# while i<n:
#     s = s + (numbers[i] - avg)**2
#     i = i+1

# print(s / n)


# FOR LOOP
# for variable in list:

# names = ["Bahareh", "Mahdieh", "Pooria", "Abolfazl", "Mahtab", "Maryam"]

# for n in names:
#     print(n)
#     print("end of the round")



# n1 = [0, 1, 2, 3, 4]
# n = range(5)
# s = 0
# numbers = []
# for i in range(5):
#     x = float(input("enter your number: "))
#     numbers.append(x)
#     s = s + x

# avg = s / n

# print(numbers)

# s = 0
# for i in numbers:
#     s = s + (i - avg)**2

# print(s / n)

# for i in range(5):
#     print(i)

# print("*"*50)
# for i in range(2, 5):
#     print(i)

# print("*"*50)
# for i in range(2, 5, 2):
#     print(i)

# print("*"*50)
# for i in range(12, 1, -1):
#     print(i)

import numpy
import statistics

numbers = []
for i in range(5):
    numbers.append(float(input("enter your number: ")))

print(numbers)

Min = numpy.amin(numbers)
Max = numpy.amax(numbers)
Avg = numpy.average(numbers)
Var = numpy.var(numbers)
Var2 = statistics.variance(numbers)


print(Min)
print(Max)
print(Avg)
print(Var)
print(Var2)
