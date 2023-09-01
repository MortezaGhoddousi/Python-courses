## Lists

# li = ["Morteza", "Javad", "Reza", "ali", "Mohammad"]

# print(li)

# print(li[1])

# li[0] = "ND"

# print(li)

# # li[2] = "ali"

# # animal = "car"
# # animal[2] = "t"
# # print(animal)

# print(li[1:4])
# print(li[3:5])
# print(li[:2])
# print(li[3:])
# print(li[:])
# print(li[4:5])
# print(li[-1])
# print(li[0:-3])

## Functions

def plusTwo(x):
    y = x+2
    print(y)
    return y

y = plusTwo(3)
print(y)


def plus(x= 0, y= 0):
    return x+y, x, y

print(plus(2, 8))

ans, x, y  = plus(2, 8)
print(ans, x, y)

def sayHello(x):
    print("Hello"+x)

sayHello(" Morteza")

# plusTwo(plus(2, 8))

ans, x, y  = plus(2, 5)
print(ans, x, y)




# # int(input("Enter your score: "))

## String Functions

# a = "morteza"

# b = a.upper()
# print(b)

# c = b.lower()
# print(c)

# d = a.capitalize()
# print(d)

# e = a.find("o")
# print(e)

# x = "Ghoddousi"
# e = x.find("o")
# print(e)

# # print(x.find())

## List Functions

# li = ["Morteza", "Javad", "Reza", "ali", "Mohammad"]
# print(len(li))

# li.append("Sam")
# print(li)

# li.insert(2, "Hasan")
# print(li)

# li.pop(3)
# print(li)

# li.pop(li.index("Mohammad"))
# print(li)