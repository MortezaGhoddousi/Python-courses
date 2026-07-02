# comparison operators

x = 4
y = 7

print("4 < 7 =", x < y)
print("4 <= 7 =", x <= y)
print("4 > 7  =", x > y)
print("4 >= 7 =", x >= y)
print("4 == 7 =", x == y)
print("4 != 7 =", x != y)

# logical operators

print("True and True =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False =", False and False)

print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)

print("not False =", not False)
print("not True =", not True)

# Exercise 

x1 = 4
x2 = 8
x3 = 6
x4 = 11
x5 = 2

avg = (x1 + x2 + x3 + x4 + x5) / 5
var = ((x1-avg)**2 + (x2-avg)**2 + (x3-avg)**2 + (x4-avg)**2 + (x5-avg)**2) / 5

print(var)
