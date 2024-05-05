# # rock paper scissors
# import random


# choices = ['rock', 'paper', 'scissors']

# while True:
#     user = input('please choose your choice (rock, paper, scissors): ').lower()

#     while True:
#         try:
#             ind = choices.index(user)
#             break
#         except:
#             user = input('please choose your choice again (rock, paper, scissors): ').lower()
            
#     computer = random.choice(choices)

#     if user == computer:
#         print(f'User has chosen {user}')
#         print(f'Computer has chosen {computer}')
#         print('Draw')
#     else:
#         if user == 'rock':
#             if computer == 'paper':
#                 print(f'User has chosen {user}')
#                 print(f'Computer has chosen {computer}')
#                 print('Computer won')
#             else:
#                 print(f'User has chosen {user}')
#                 print(f'Computer has chosen {computer}')
#                 print('User won')
                
#         if user == 'paper':
#             if computer == 'scissors':
#                 print(f'User has chosen {user}')
#                 print(f'Computer has chosen {computer}')
#                 print('Computer won')
#             else:
#                 print(f'User has chosen {user}')
#                 print(f'Computer has chosen {computer}')
#                 print('User won')
                
#         if user == 'scissors':
#             if computer == 'rock':
#                 print(f'User has chosen {user}')
#                 print(f'Computer has chosen {computer}')
#                 print('Computer won')
#             else:
#                 print(f'User has chosen {user}')
#                 print(f'Computer has chosen {computer}')
#                 print('User won')
                
#     quitDecision = input('If you want to quit press "q": ')
#     if quitDecision == 'q':
#         break
    
# print('End of the game!')
        
        
# Lists 

names = ['morteza', 'moslem', 'mahtab', 'hossein']

print(names)
print(names[0])

print(names[0:3])

print(names[2:4])
print(names[2:])

print(names[0:2])
print(names[:2])

print(names[:])

print(names[3])
print(names[-1])

print(names[-2:])

print(names[-3:-1])