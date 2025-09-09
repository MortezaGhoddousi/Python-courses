
# Comparison Operators
x = 4
y = 9

z = x < y
# print(str(x) + ' < ' + str(y) + ' = ')
print(f"{x} < {y} ==> {z}")

z = x <= y
print(f"{x} <= {y} ==> {z}")

z = x > y
print(f"{x} > {y} ==> {z}")

z = x >= y
print(f"{x} >= {y} ==> {z}")

z = x == y
print(f"{x} == {y} ==> {z}")

z = x != y
print(f"{x} != {y} ==> {z}")

# Logical Operators

x = True
y = True
z = x and y
print(f"{x} and {y} => {z}")

x = True
y = False
z = x and y
print(f"{x} and {y} => {z}")

x = False
y = True
z = x and y
print(f"{x} and {y} => {z}")

x = False
y = False
z = x and y
print(f"{x} and {y} => {z}")


x = True
y = True
z = x or y
print(f"{x} or {y} => {z}")

x = True
y = False
z = x or y
print(f"{x} or {y} => {z}")

x = False
y = True
z = x or y
print(f"{x} or {y} => {z}")

x = False
y = False
z = x or y
print(f"{x} or {y} => {z}")

x = True
z = not x
print(f"not {x} => {z}")

x = False
z = not x
print(f"not {x} => {z}")

# exercise
print(f"True and 4 <= 4 => {True and 4 <= 4}")

## # Programming Languages' Structures

## # Selections' Structure
## # if statement

# if boolean:
#     body
#     body
#     body

age = 15

if age >= 18:
    print('You are adult')
elif age >= 10 and age < 18:
    print('You are teenager')
else:
    print('You are child')

print('end of the statement')

# exercise
x = 174
y = 74

if x>=y:
    print(x)
else:
    print(y)


## # Selections' Structure
## # while loop

# while boolean:
#     body
#     body
#     body

i = 0
while i<3:
    print('hello world!')
    i = i+1

print('end of the loop')

# exercise
admin = '1234'
userPassword = input('enter your password:')

while admin != userPassword:
    print('wrong password. Trye again!')
    userPassword = input('enter your password:')

print('access granted!')


# exercise
i = 10
while i<100:
    print(i)
    i = i+2

print('end of the loop')

# exercise
import random

goal = input('left or right: ')
player = random.randint(0, 1)

if player == 0:
    player = 'left'
else:
    player = 'right'


if goal == player:
    print('bot win')
else:
    print('you win')
