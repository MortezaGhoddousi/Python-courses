# Print function
print("hello world!")
print(3)
print(4.5)
print(True)
print(False)


# # Variables
# String
firstName = "Morteza"
lastName = 'Ghoddousi'

# print(firstName - lastName)

# Integer
age = 31
weight = 82

# Float
height = 1.86

# Boolean
isMale = True

print("Morteza")
print(firstName)
print(lastName)
print(age)
print(weight)
print(height)
print(isMale)

# Mathematical Operators
x = 6
y = 3.75

z = x + y
print("x =", x)
print("y =", y)
print("x + y =", z)

z = x - y
print("x =", x)
print("y =", y)
print("x - y =", z)

z = x * y
print("x =", x)
print("y =", y)
print("x * y =", z)

z = x / y
print("x =", x)
print("y =", y)
print("x / y =", z)

z = x ** y
print("x =", x)
print("y =", y)
print("x ** y =", z)

z = x % y
print("x =", x)
print("y =", y)
print("x % y =", z)

# Exercise

midTermScore = 17.5
finalScore = 19

average = (midTermScore + finalScore) / 2

print('Average =', average)

# type function
# String
firstName = "Morteza"
lastName = 'Ghoddousi'

# print(firstName - lastName)

# Integer
age = 31
weight = 82

# Float
height = 1.86

# Boolean
isMale = True

print(firstName, type(firstName))
print(lastName, type(lastName))
print(age, type(age))
print(weight, type(weight))
print(height, type(height))
print(isMale, type(isMale))

# concatenation operator
stringX = '7'
stringY = '8'

z = stringX + stringY
print(z, type(z))

intX = int(stringX) 
intY = int(stringY) 

z = intX + intY
print(z, type(z))

floatX = float(stringX)
floatY = float(stringY)

z = floatX + floatY
print(z, type(z))

z = str(z)
print(z, type(z))

x = 1

z = bool(x)
print(z, type(z))
