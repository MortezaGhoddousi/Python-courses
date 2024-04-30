# While loops 

# for i in range(3):
#     print(i)
    
# i = 0

# while i < 3:
#     print(i)
#     i = i+1
    
#ex 1

# password = '123'

# geuss = input('enter your password: ')

# while geuss != password:
    
#     # List initialization
#     input1 = [int(geuss)]
    
#     # Using map
#     output = list(map(int, str(input1[0])))
#     while len(output) > 3:
#         print('Invalid input')
#         geuss = input('enter your password again: ')
#         # List initialization
#         input1 = [int(geuss)]
        
#         # Using map
#         output = list(map(int, str(input1[0])))
            
#     print('Wrong password!')
#     geuss = input('enter your password again: ')
    
# print('Access granted')

# If statements

# if True:
#     print('Condition is TRUE')
# else:
#     print('Condition is False')
    
# age = int(input("Enter your age: "))

# if age < 18 and age >= 10:
#     print("Teenager")
# elif age < 10:
#     print("Child")
# else:
#     print('Adult')
    

# print('End of the if statement')
    
#ex 2

import math
# import random

# option = ['rock', 'paper', 'scissors']
# print(random.randint(0, 2))


x1 = float(input('Enter your first score: '))
x2 = float(input('Enter your second score: '))
x3 = float(input('Enter your third score: '))

scores = [x1, x2, x3]

# i = 0
Min = math.inf
Max = -1*math.inf

# while i<len(scores):
#     if scores[i] < Min:
#         Min = scores[i]
        
#     if scores[i] > Max:
#         Max = scores[i]
        
#     i = i+1

for i in scores:
    if i < Min:
        Min = i
        
    if i > Max:
        Max = i
    
print(f"Maximum number is: {Max}")
print(f"Minimum number is: {Min}")
    

