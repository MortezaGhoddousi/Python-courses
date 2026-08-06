def f(x, y):
    z = x**2 + 2*x*y + y**2
    return z

print(f(2, 9))

g = f(2, 9) + 9
print(g)

def say_hello1():
    print("hello world")

def say_hello2(fname):
    print(f"hello {fname}")

def say_hello3():
    return "hello world"

def say_hello4(fname):
    return f"hello {fname}"

say_hello1()

say_hello2("Morteza")

print(say_hello3())

print(say_hello4("Mohsen"))




