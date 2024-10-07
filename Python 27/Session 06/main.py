# N = 4

# Sum = 0

# i = 0

# Min = 0
# Max = 0

# myNumbers = open('./numbers.txt', 'w')
# while i<N:
#     x = int (input('enter the number: '))
    
#     myNumbers.write(f'{x} \n')
#     if i == 0:
#         Min = x
#         Max = x
    
#     Sum = Sum + x
    
#     if x > Max:
#         Max = x
        
#     if x < Min: 
#         Min = x
        
#     i = i+1
        
# Average = Sum / N

# myNumbers.close()

# myNumbers = open('./numbers.txt', 'r')
# Sum = 0

# for line in myNumbers:
#     print(line)
#     Sum = Sum + (int(line)-Average)**2
    
# Var = Sum / N


# print(f"Average of the numbers: {Average}")
# print(f"Variance of the numbers: {Var}")
# print(f"Minimum of the numbers: {Min}")
# print(f"Maximum of the numbers: {Max}")
        
        
# myNumbers = [20, 18, 16, 15, 20, 14, 10]

# Sum = 0
# i = 0
# while i<7:
#     Sum = Sum + myNumbers[i]
#     i = i+1
    
    
# print(Sum/7)

# MyInformation = ['Morteza', 'Ghoddousi', 30, 1.85, 92, True]

# print(MyInformation)
# # MyInformation.append('IR')
# MyInformation.insert(2, 'IR')
# print(MyInformation)
# MyInformation.pop(MyInformation.index(92))
# print(MyInformation)

# print(MyInformation[0])
# print(MyInformation[1])
# print(MyInformation[2])
# print(MyInformation[3])
# print(MyInformation[4])
# print(MyInformation[5])


N = 5

numbers = []

i = 0
while i<N:
    numbers.append(float(input('enter the number: ')))
    i = i+1 
    
print(numbers)

import numpy

print(numpy.min(numbers))
print(numpy.max(numbers))
print(numpy.average(numbers))
print(numpy.var(numbers))
print(numpy.std(numbers))


i = 0
Sum = 0

Max = numbers[0]
Min = numbers[0]

while i<N:
    Sum = Sum + numbers[i]
    
    if numbers[i] > Max:
        Max = numbers[i]
        
    if numbers[i] < Min:
        Min = numbers[i]
        
    i = i+1
        
Average = Sum / N

i = 0
Sum = 0

while i<N:
    Sum = Sum + (numbers[i] - Average)**2
    i = i+1
    
Variance = Sum/N 

STD = numpy.sqrt(Variance)

print(Max)   
print(Min)   
print(Average)   
print(Variance)
print(STD)
