distance = 14
unit = 'km'

print(str(distance)+unit)
print(f'{distance}'+unit)

# Boolean
x = 5
y = 9

print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)

print(type(x < y))

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)

print(not(True and False))

print((True and False) or (True or False))


print('============================================')

import numpy as np

x = int(input('Enter the number: '))
y = np.mod(x, 2)

if y==0:
    print('Even')
else:
    print('Odd')