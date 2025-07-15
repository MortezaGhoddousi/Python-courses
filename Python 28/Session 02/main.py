# Variables

# String
firstName = "Morteza"
lastName = "Ghoddousi"

# Integer
age = 31
weight = 84

# Float
height = 1.86

# Boolean
isMale = True

# Print Function

print("Morteza")
print(firstName, lastName)

print("age:", age)

# Math Operators

x = 7
y = 3.25

z = x + y
print("x + y = ", z)

z = x - y
print("x - y = ", z)

z = x * y
print("x * y = ", z)

z = x / y
print("x / y = ", z)

z = x % y
print("x % y = ", z)

z = x ** y
print("x ** y = ", z)

# Concatenation operator
print(firstName + lastName)

# type function

print(type(firstName))
print(type(lastName))
print(type(age))
print(type(weight))
print(type(height))
print(type(isMale))


# exchangin between variable's types
h = 5
print("h: ", h)
print("type of h", type(h))

h1 = float(h)
print("h1: ", h1)
print("type of h1", type(h1))

h2 = str(h1)
print("h2: ", h2)
print("type of h2", type(h2))

h3 = int("7")
print("h3: ", h3)
print("type of h3", type(h3))

# int("hello world!")