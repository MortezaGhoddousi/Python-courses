print('Hello world!')
fname = input('Enter your name: ')
# age = input('Enter your age: ')
# age1 = int(age)
# age = int(age)

age = int(input('Enter your age: '))

print(type(age))
# print(type(age1))

# print(2+2)
# print('morteza '+'Ghoddousi')

# print(age+'2')
# print(age1+2)
print(age+2)

print(float(age))
print(type(float(age)))

# float(fname)

print('my age is: '+str(age))

# Comparison Operators 

x = 10
y = 5
print(x<y) #Lower than
print(x<=y) # Lower than or Equal
print(x>y) # Greater than
print(x>=y) # Greater than or Equal
print(x==y) # Equal
print(x!=y) # Not equal

print(type(x<y)) 

# Logical Operators 

print(True and False)
print(False and True)
print(True or False)
print(False or True)

temp = 40
presence = True
print((temp>30) and presence)