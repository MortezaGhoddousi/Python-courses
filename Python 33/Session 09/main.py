<<<<<<< HEAD
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
=======
def f(x):
    z = x+4
    return z

print(f(3))

def g(x, y):
    z = x**2 + 3*y
    return z

x = g(1, 5)

print(x)

def sayHello(name):
    print("hello " + name)

sayHello("Morteza")
sayHello("Mohsen")

def sayHello2():
    return "this function is invoked"

print(sayHello2())

def sayHello3():
    print("hello from this function")

sayHello3()


def cal_root(a, b, c):
    delta = b**2 - (4*a*c)
    if delta > 0:
        x1 = (-b+delta**0.5)/(2*a)
        x2 = (-b-delta**0.5)/(2*a)
        return [x1, x2]
    elif delta == 0:
        x = (-b)/(2*a)
        return x
    else:
        return "no root"

a1 = 4
b1 = 4
c1 = 1
print(cal_root(a1, b1, c1))
>>>>>>> 1a43faee5a04a80bd8e8e96bd37d8ce53618e653
