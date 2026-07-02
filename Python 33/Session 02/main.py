first_name = "Morteza" # String
age = 31 # Integer
weight = 83 # Integer
height = 1.86 # Float
is_male = True # Boolean


# print function
print(first_name)
print("Hello world!")
print(4)

# mathematical operators
x = 4
y = 7

z = x+y
print(str(x) + "+" + str(y) + "=" +  str(z))

z = x-y
print(str(x) + "-" + str(y) + "=" +  str(z))

z = x*y
print(str(x) + "*" + str(y) + "=" +  str(z))

z = x/y
print(str(x) + "/" + str(y) + "=" +  str(z))

z = x%y
print(str(x) + "%" + str(y) + "=" +  str(z))

z = x**y
print(str(x) + "**" + str(y) + "=" +  str(z))

x = x+3

# concatenation operator
last_name = "Ghoddousi"

print(first_name, last_name)
full_name = "Morteza Ghoddousi"
full_name1 = first_name+" "+last_name
print(full_name1)

h = "hello" + "4"
print(h)

h1 = "Hello" + str(x) # "7"
print(h1)

x = "8"
print(type(x))
x = int(x)
print(type(x))
y = 4.5
print(type(y))

z = float(x) + y
print(z)

print(type(is_male))

# print("enter your name: ")
your_name = input("enter your name: ")
print(your_name)

print(type(your_name))

your_age = input("enter your age: ")
print(your_age)

print(type(your_age))

your_age = int(your_age)
print(type(your_age))
