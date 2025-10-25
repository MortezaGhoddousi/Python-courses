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