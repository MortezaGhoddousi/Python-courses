# # Exercise 1
# a = int(input('enter first parameter: '))
# b = int(input('enter second parameter: '))

# # c2 = a2 + b2
# c2 = a**2 + b**2
# c = c2**0.5
# print(c)

# # Exercise 2
# for i in range(10, 100):
#     c = False
#     j = 2
#     while j<i:
#         if i%j == 0:
#             c = True
#             break
#         j = j+1
#     if c:
#        print(f"{i} is not prime")
#     else:
#        print(f"{i} is prime")


# Functions
# define = برای بار اول تعریف کردن

def f(x):
    # local variables
    y = 2*x**2 + 5*x + 3
    return y

print(f(4))
# global variables
x = f(4)
# print(y)
print(x)
x = f(2)
print(x)

# 1- no input, no output
def sayHello():
    print("Hello world!")
    print("end of the function")

sayHello()
sayHello()

# 2- function with inputs and without output
def sayHello2(name1, name2):
    print(f"Hello mr {name1}")
    print(f"Hello mr {name2}")
    print("end of the function")

sayHello2("Morteza", "AmirALi")

# 3- function without inputs, with an output
def sayHello3():
    return 'hello world!'

x = sayHello3()
print(x)

# 4- function with inputs, with an output
def sayHello3(name):
    return f'hello mr {name}'

x = sayHello3("Morteza")
print(x)


def fithTriangle(a, b):
    c = (b**2 + a**2)**0.5
    return c

print(fithTriangle(3, 4))
print(fithTriangle(6, 9))
print(fithTriangle(12, 19))

def calPrimeNumbers(x, y):
    for i in range(x, y+1):
        c = False
        j = 2
        while j<i:
            if i%j == 0:
                c = True
                break
            j = j+1
        if c:
            print(f"{i} is not prime")
        else:
            print(f"{i} is prime")

calPrimeNumbers(10, 99)
calPrimeNumbers(3, 10)