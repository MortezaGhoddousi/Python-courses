import random

options = ['rock', 'paper', 'scissors']

bot = random.choice(options)
player = input('enter your choice: ')

if bot == player:
    print('draw')
elif bot == 'rock' and player == 'paper':
    print('player Won')
elif bot == 'rock' and player == 'scissors':
    print('bot Won')
elif bot == 'paper' and player == 'scissors':
    print('player Won')
elif bot == 'paper' and player == 'rock':
    print('bot Won')
elif bot == 'scissors' and player == 'rock':
    print('player Won')
elif bot == 'scissors' and player == 'paper':
    print('bot Won')

print(bot)
print(player)