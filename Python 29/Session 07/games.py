# # rock, paper, scissors
# from random import choice

# options = ['rock', 'paper', 'scissors']

# bot = choice(options)
# player = input('enter your choice(rock, paper, scissors): ')

# print(f'player choose: {player}')
# print(f'bot choose: {bot}')

# if player == bot:
#     print('draw')
# elif player == 'rock' and bot == 'scissors':
#     print('player won')
# elif player == 'rock' and bot == 'paper':
#     print('bot won')
# elif player == 'paper' and bot == 'rock':
#     print('player won')
# elif player == 'paper' and bot == 'scissors':
#     print('bot won')
# elif player == 'scissors' and bot == 'paper':
#     print('player won')
# elif player == 'scissors' and bot == 'rock':
#     print('bot won')

# # goal   
# from random import choice

# goal = ['left', 'right']

# player = input('enter your choice(left, right): ').lower()
# while not player in goal:
#     print('wrong choice. try again!')
#     player = input('enter your choice(left, right): ').lower()

# bot = choice(goal)

# print(f'player choose: {player}')
# print(f'bot choose: {bot}')

# if player == bot:
#     print('bot won')
# else:
#     print('player won')