# FUNCTION
print("start of the script")

def hello ():
    print("start of the function")
    print("Hello")
    print("end of the function")

def hello2(name1, name2):
    print("hello " + name1 + " and " + name2 )

def hello3 ():
    print("third type of function")
    return "hello world"

def hello4 (name1, name2):
    return name1 + name2



hello()
print("end of the script")
hello()


hello2("Morteza", "Maryam")
hello2("Mahtab", "Abolfazl")

x = hello3 ()
# x = "hello world"

print(x)

# print(name1 + name2)
print(hello4("Morteza", "Iman"))


def sumTwo (x, y):
    return x + y


a = 4
b = 6

z = sumTwo(a, b)

print(z)

print(sumTwo(5, 9))
print(sumTwo(15, 79))

def calAvg(a, b, c):
    s = a+b+c
    return s/3

# print(s)

print(calAvg(4, 8, 3))
print(calAvg(14, 45, 21))

numbers = [4, 7, 8, 9, 1, 2, 45, 12, 9, 15, 18, 23]

import numpy
print(numpy.average(numbers))
print(numpy.amax(numbers))
print(numpy.amin(numbers))
print(numpy.var(numbers))

print(numpy.pi)


import functions
print(functions.calAvgList(numbers))
print(functions.calMax(numbers))
print(functions.calMin(numbers))
print(functions.calVar(numbers))
print(functions.Pi_number)



