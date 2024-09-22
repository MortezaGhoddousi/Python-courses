import random

def checkWin(player, bot):
    if player == bot:
        return 'Draw'
    elif player == 'rock' and bot == 'paper':
        return 'Bot Won'
    elif player == 'rock' and bot == 'scissors':
        return 'Player Won'
    elif player == 'paper' and bot == 'rock':
        return 'Player Won'
    elif player == 'paper' and bot == 'scissors':
        return 'Bot Won'
    elif player == 'scissors' and bot == 'rock':
        return 'Bot Won'
    elif player == 'scissors' and bot == 'paper':
        return 'Player Won'
    

options = ['rock', 'paper', 'scissors']

bot = random.choice(options)

player = input('choose your choice: ')
player = player.lower()

while True:
    try:
        options.index(player)
        break
    except:
        print('You have to choose only from your options!')
        player = input('choose your choice: ')
        player = player.lower()



print(checkWin(player, bot))
print(f"Player has chosen {player}")
print(f"Bot has chosen {bot}")
 



