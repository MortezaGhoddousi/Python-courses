
def f(x, y):
    z = x**2 + 3*x*y + 3*y + 4
    return z
    



x = f(4,5)
print(f(4,5))
print(x)

def rect(w, l):
    area = w*l
    primeter = 2*(l+w)
    
    return [area, primeter]

print(rect(3, 8))

[a, p] = rect(4, 5)
output = rect(4, 5)

print(f"the area of the rectangle is {a} and the primeter of it is {p}")
print(f"the area of the rectangle is {output[0]} and the primeter of it is {output[1]}")
print(rect(4, 5))

fname = 'Morteza'
myli = [fname]


# def print(w, l):
#     area = w*l
#     primeter = 2*(l+w)
    
#     return [area, primeter]

# print(3)
# lname = c+4

def sayHello ():
    print('hello guys')
    
sayHello()
sayHello()
sayHello()