# age = int(input('enter your age: '))

# if age >= 18:
#     print('first condition is True')
#     print('User is an Adult')
# elif age < 18 and age > 10:
#     print('second condition is True')
#     print('User is a Teenager')
# else:
#     print('both conditions are False')
#     print('User is a Child')
    
# print('end')

x = float(input('enter your first number: '))
y = float(input('enter your second number: '))
z = float(input('enter your third number: '))

Max = -100000000

if x > Max:
    Max = x

if y > Max:
    Max = y
    
if z > Max:
    Max = z
    
print(Max)