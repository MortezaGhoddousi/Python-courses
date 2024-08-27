# name1 = 'AmirALi'
# name2 = 'Nima'
# name3 = 'Amin'
# name4 = 'Shady'
# name5 = 'Ensieh'
# name6 = 'Mohaddeseh'

# print(name1)
# print(name2)
# print(name3)
# print(name4)
# print(name5)
# print(name6)

# names = ['AmirALi', 'Nima', 'Amin', 'Shady', 'Ensieh', 'Mohaddeseh']

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])

# newName = input('enter your name: ')
# print(names)
# names.append(newName)
# print(names)
# names.insert(1, newName)
# print(names)
# names.pop(2)
# print(names)

# print(names.index('Shady'))
# names.pop(names.index('Shady'))
# print(names)

# print(len(names))
# print(len('Morteza'))

# names[0] = 'Iman'
# print(names)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers1 = range(10)
# numbers2 = range(3, 6)


# i = 0

# while i<3:
#     print('hello')
#     i = i+1
    
# print('end')

import math

imax = int(input('enter how many numbers do you have: '))

i = 0
Max = -1*math.inf
Min = math.inf

while i < imax:
    x = float(input('enter your number: '))
    if x<Min:
        Min = x
        
    if x>Max:
        Max = x
        
    i = i+1
    
print(Min)
print(Max)

