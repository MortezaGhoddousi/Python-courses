# def factorial(x=1, *arg):
#     print(x, arg)
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
    
    
# print(factorial(5))
# print(factorial())
# print(factorial(5, 1, 2, 3, 4))

def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    
    
my_func(2, 3, 4, 5, 6, a=7, b=8)

import numpy as np

x = np.array([[0, 0], [1, 1]], dtype=float)

print(x)

import Human1
        
morteza = Human1.Human('Morteza', 'Ghoddousi', 30)
mahtab = Human1.Human('Mahtab', 'Asadi', 19)
moslem = Human1.Human('Moslem', 'HasanNezhad', 20)

morteza.sayHello()
mahtab.sayHello()
moslem.sayHello()

myRect = Human1.Rectangle(2, 3)
print(myRect.calArea())
print(myRect.calPrimeter())
print(myRect.calvolume())




