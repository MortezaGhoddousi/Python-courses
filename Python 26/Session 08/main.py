for i in range(10):
    print(i)
    
for i in 'Morteza':
    print(i)
    
fname = 'Morteza'
print(fname[3])

print(fname.upper())
print(fname.lower())
print(fname.capitalize())
print(fname.find('r'))

# fname[3] = 'f'

myList = ['M', 'o', 'r', 't', 'e', 'z', 'a']
myList[3] = 'f'

print(myList)

# Functions

def f(x, y):
    return x+y

print(f(2, 8))
z = f(3, 5)
print(z)

import numpy

def roots(a, b, c):
    delta = b**2 - (4*a*c)
    if delta > 0:
        x1 = (-b + numpy.sqrt(delta))/(2*a)
        x2 = (-b - numpy.sqrt(delta))/(2*a)
        return [x1, x2]
    elif delta == 0:
        return (-b/(2*a))
    else:
        return False
    
print(roots(2, 4, 1))
print(roots(1, 4, 4))
print(roots(1, 4, 8))

x = roots(1, 4, 2)
print(type(x))

if x == False:
    print('There are no roots!')
elif isinstance(x, list):
    print(f'the roots are: {x[0]}, {x[1]}')
elif isinstance(x, float):
    print(f'the root is: {x}')


