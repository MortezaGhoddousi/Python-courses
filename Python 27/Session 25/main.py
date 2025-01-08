# def mappedFunction(x):
#     return x**2

# def filteredFunction(x):
#     return x>0


# myNumbers = [4, 2, 1, 5, 0, 10, 14]


# poweredNumbers = []
# for i in myNumbers:
#     poweredNumbers.append(i**2)
    
# print(poweredNumbers)

# mappedNumbers = list(map(mappedFunction, myNumbers))

# print(mappedNumbers)

# filteredNumbers = list(filter(filteredFunction, myNumbers))

# print(filteredNumbers)


# def plusNumbers (x=0, *y, **z):
#     print(y)
#     print(z)
    
#     Sum = x
#     for i in y:
#         Sum = Sum + i
    
#     return Sum

# # print(plusNumbers (2, 3))
# # print(plusNumbers (2))
# print(plusNumbers (2, 3, 4, 7, 8, a=9, b=15))

from MATH import Python27, Python27_2

x = Python27([4, 7, 15, 2])
y = Python27([1, 3, 5, 2])

print(x.calAverage())
# print(y.calAverage())

print(x.calVariance())
print(x.calMax())
print(x.calMin())
print(x.calSTD())

z = Python27_2()

print(z.calAverage([4, 7, 15, 2]))
print(z.calVariance([4, 7, 15, 2]))
print(z.calMax([4, 7, 15, 2]))
print(z.calMin([4, 7, 15, 2]))
print(z.calSTD([4, 7, 15, 2]))

class extendedPython27(Python27_2):
    def __init__(self):
        pass
    
    def mappedList(self, numbers):
        poweredNumbers = []
        for i in numbers:
            poweredNumbers.append(i**2)
            
        return poweredNumbers
    
a = extendedPython27()

print(a.calAverage([4, 7, 15, 2]))
print(a.calVariance([4, 7, 15, 2]))
print(a.calMax([4, 7, 15, 2]))
print(a.calMin([4, 7, 15, 2]))
print(a.calSTD([4, 7, 15, 2]))
print(a.mappedList([4, 7, 15, 2]))






