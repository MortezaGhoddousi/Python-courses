# Custom Functions

# def f(x):
#     y = 2*x+3
#     print(y)

# f(6)
# f(9)



# def sayHello(name1="Morteza", name2="Iman"):
#     print(f"Hello {name1} and {name2}")

# sayHello("Morteza", "Elina")
# sayHello("Elina")

# def f(x):
#     y = 2*x+3
#     return y
    
# y = f(6)
# print(y+18)
# print(f(6)+18)


def two_num(x, y):
    a = x+y
    b = x-y
    return a, b


f, h = two_num(5, 3)

print(f, h)