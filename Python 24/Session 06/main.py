print('========================================')
print('Comparison Operators')

x = 4
y = 3

print(f'{x} > {y} => {x > y}')
print(f'{x} >= {y} => {x >= y}')
print(f'{x} < {y} => {x < y}')
print(f'{x} <= {y} => {x <= y}')
print(f'{x} == {y} => {x == y}')
print(f'{x} != {y} => {x != y}')

print('========================================')
print('Logical Operators')

print(f'True and True => {True and True}')
print(f'True and False => {True and False}')
print(f'False and True => {False and True}')
print(f'False and False => {False and False}')

print(f'True or True => {True or True}')
print(f'True or False => {True or False}')
print(f'False or True => {False or True}')
print(f'False or False => {False or False}')

print(f'not False => {not False}')
print(f'not True => {not True}')

print (not ((4 > 5) and True and (5 == 5)))


print('========================================')
print('List')

name1 = 'Morteza'
name2 = 'Mahtab'
name3 = 'Moslem'
name4 = 'Mohammmad'

print(name2)

names = ['Morteza', name2, name3, name4, 15, 156.7, True, [14, 15, 16]]
print(names)

print(names[1])
print(names[7][2])

print('========================================')
print('For loops')

for i in names:
    print(i)
    
print('End of the loop')

print('========================================')
print('Ex 1')

print('START')

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))

scores = [a, b, c]
print(len(scores))
Sum = 0

for i in scores:
    print(i)
    Sum = Sum+i
    
print(Sum / len(scores))

print('END')

print('========================================')
print('range funciton')

for i in range(4):
    print(i)
    
    
for i in range(3):
    print('hello')
    



    
    
    
