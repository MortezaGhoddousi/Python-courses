# Comparison Operators

print("comparison operators")
x = 4
y = 7

z = x > y
print(str(x)+" > "+str(y)+" = ",z)

z = x >= y
print(str(x)+" >= "+str(y)+" = ",z)

z = x < y
print(str(x)+" < "+str(y)+" = ",z)

z = x <= y
print(str(x)+" <= "+str(y)+" = ",z)

z = x == y
print(str(x)+" == "+str(y)+" = ",z)

z = x != y
print(str(x)+" != "+str(y)+" = ",z)

# Logical Operators
print("logical operators")

x = True
y = True
z = x and y
print(x, "and", y, " = ", z)

x = True
y = False
z = x and y
print(x, "and", y, " = ", z)

x = False
y = True
z = x and y
print(x, "and", y, " = ", z)

x = False
y = False
z = x and y
print(x, "and", y, " = ", z)

x = True
y = True
z = x or y
print(x, "or", y, " = ", z)

x = True
y = False
z = x or y
print(x, "or", y, " = ", z)

x = False
y = True
z = x or y
print(x, "or", y, " = ", z)

x = False
y = False
z = x or y
print(x, "or", y, " = ", z)

x = True
z = not x
print("not ", x, " = ", z)

x = False
z = not x
print("not ", x, " = ", z)

# example
print(not((51 == 17) and True or (4 >= 4)))

# example
x = 31.2
print(x>30)

message = "Debuging"

print (5+3)

revenue = 300
print(revenue)

# print("Enter midterm score: ")
midTerm = input("Enter midterm score: ")
final = float(input("Enter final score: "))

midTerm = float(midTerm)
Sum = midTerm+final
print("sumation of midterm score and final = ", Sum)
print("Average of midterm and final scores = ", Sum / 2)