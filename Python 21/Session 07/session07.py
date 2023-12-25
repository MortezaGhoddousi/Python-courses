import random

# names = ['morteza', 'Hadi', 'Honey']
# print(names[0])

# options = ['paper', 'rock', 'scissors', 'Rock', 'Paper', 'Scissors', 'ROCK', 'PAPER', 'SCISSORS']
# options = ['paper', 'rock', 'scissors']

# choice = random.randint(0, 2)
# print(choice)
# print(options[choice])
# range(3) [0, 3)
# print(random.choice(options))
# pc = options[1]
# player = input('enter your choice: ')
# player = player.lower()

# if player in options:
#     if player == pc:
#         print('draw')
#     elif player == options[0]:
#         print('player won')
#     elif player == options[2]:
#         print('pc won')
# else:
#     print('invalid input')

# if pc == player:
#     print('draw')
# elif player == options[0]:
#     print('player won')
# elif player == options[2]:
#     print('pc won')


# options = ['paper', 'rock', 'scissors']

# napar = True
# while napar:

#     player = input('enter your choice: ')
#     player = player.lower()
#     if player == 'q':
#         napar = False

#     while not player in options:
#         print('Invalid input')
#         player = input('enter your choice again: ')
#         player = player.lower()
#         if player == 'q':
#             napar = False
#             break
        
#     pc = random.choice(options)

#     print(pc)

#     if pc == player:
#         print('Draw')
#     elif pc == options[0] and player == options[1]:
#         print('PC won')
#     elif pc == options[0] and player == options[2]:
#         print('Player won')
#     elif pc == options[1] and player == options[0]:
#         print('Player won')
#     elif pc == options[1] and player == options[2]:
#         print('PC won')
#     elif pc == options[2] and player == options[0]:
#         print('PC won')
#     elif pc == options[2] and player == options[1]:
#         print('Player won')
        
        
num_stu = int(input('Enter the number of students: '))
i = 0
min_num = 21
max_num = -1

my_list = []

while i<num_stu:
    x = random.randint(0, 20)
    # my_list[i] = x
    my_list.append(x)
    # print(x)
    if x<min_num:
        min_num = x
    if x>max_num:
        max_num = x
    i = i+1
    
print(f'My list is: {my_list}')
print(f'Minimum number is: {min_num}')
print(f'Maximum number is: {max_num}')