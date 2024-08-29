i = 0
while i<3:
    print('Hello')
    i = i+1
    
print('end')

for i in [0, 10, 20]:
    print('Hello')
    
print('end')

for i in range(100):
    print('hello')
    print(i)

print('end')

names = ['Morteza', 'AmirHossein', 'Nima', 'Amin', 'Ensieh', 'Mohaddeseh']

for i in names:
    print(i)

import math
numbers = [4, 16, 18, 20, 20, 19.5, 2, 0, 15, 16, 16.75]

Max = -1*math.inf
Min = math.inf

Sum = 0

for i in numbers:
    Sum = Sum + i
    if i < Min:
        Min = i
    if i > Max:
        Max = i
    
avg = Sum / len(numbers)   

Sum = 0
        
for i in numbers:
    Sum = Sum + (i-avg)**2

var = Sum / len(numbers) 

print(Min, Max, avg, var)

import numpy

numbers = [4, 16, 18, 20, 20, 19.5, 2, 0, 15, 16, 16.75]

print(numpy.min(numbers), numpy.max(numbers), numpy.average(numbers), numpy.var(numbers))

names = ['Morteza', 'AmirHossein', 'Nima', 'Amin', 'Ensieh', 'Mohaddeseh']

print(names[2])

newNames = [names[1], names[2], names[3]]

newNames1 = names[1:4]

print(newNames)
print(newNames1)

print(names[4:6])
print(names[4:])

print(names[0:2])
print(names[:2])

print(names[:])

print(names[5])
print(names[-1])

print(names[-2])

print(names[-3])
print(names[-4])
print(names[-5])
print(names[-6])

# Example 01

x = int(input('enter your number: '))
p = 1
for i in range(1, x+1):
    p = p*i
print(p)


# Example 02

numbers = [4, 16, 18, 20, 20, 19.5, 2, 0, 15, 16, 16.75]
numbers.sort(reverse=False)

# numbers.reverse()

print(numbers)

numbers = [4, 16, 18, 20, 20, 19.5, 2, 0, 15, 16, 16.75]

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[j], numbers[i] = numbers[i], numbers[j]

print(numbers)