import random
import functions


## define all cards in 4 separated lists
Del = range(2, 15)
Pik = range(2, 15)
Gishniz = range(2, 15)
Khesht = range(2, 15)

# DelCards = []
# for i in Del:
#     DelCards.append(str(i) + ' del')
    
    
## adding type of each category to the cards
DelCards = [str(i)+' del' for i in Del]
PikCards = [str(i)+' pik' for i in Pik]
GishnizCards = [str(i)+' gishniz' for i in Gishniz]
KheshtCards = [str(i)+' khesht' for i in Khesht]

# allCards = [DelCards, PikCards, GishnizCards, KheshtCards]

allCards = []

## merging all 4 different cards into a single list
for i in range(13):
    allCards.append(DelCards[i])
    allCards.append(PikCards[i])
    allCards.append(GishnizCards[i])
    allCards.append(KheshtCards[i])
      
# print(allCards)

## select the roler
hakem = random.randint(1, 4)
# hakem = 1

## define background
zamineha = ['del', 'pik', 'gishniz', 'khesht']
if hakem == 1: 
    hokm = input('Hokm ra entekhab kon: ')
else:
    hokm = random.choice(zamineha)
  
print(hokm)
## deal the cards
[player, bot1, bot2, bot3] = functions.splitTheCards(allCards)

## classify all different types of cards 
player = functions.sortCards(player, hokm)
bot1 = functions.sortCards(bot1, hokm)
bot2 = functions.sortCards(bot2, hokm)
bot3 = functions.sortCards(bot3, hokm)


winner = hakem

team1 = 0
team2 = 0


## start the game
while True:
    
    ## player 1
    if winner == 1:
        print(player)
        ch = input('card khod ra entekhab namayid: ')
        print(ch)
        zamine = ch.split(" ")[1]
        
        ## removing played card
        if zamine == 'del':
            player[0].remove(ch)
        elif zamine == 'pik':
            player[1].remove(ch)
        elif zamine == 'gishniz':
            player[2].remove(ch)
        elif zamine == 'khesht':
            player[3].remove(ch)
            
     
        [bot1, choice1] = functions.chooseCard(bot1, zamine)
        print('bot1 ', choice1)
        [bot2, choice2] = functions.chooseCard(bot2, zamine)
        print('bot2 ', choice2)
        [bot3, choice3] = functions.chooseCard(bot3, zamine)
        print('bot3 ', choice3)
        
        ## check who won the round
        winner = functions.checkWinRound(ch, choice1, choice2, choice3, zamine)
        print(winner)
        if winner == 1 or winner == 3:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
        print(team1, team2)  
        
    ## bot1
    elif winner == 2:
        zamine = random.choice(zamineha)
        print(zamine)
        [bot1, choice1] = functions.chooseCard(bot1, zamine)
        print('bot1 ', choice1)
        [bot2, choice2] = functions.chooseCard(bot2, zamine)
        print('bot2 ', choice2)
        [bot3, choice3] = functions.chooseCard(bot3, zamine)
        print('bot3 ', choice3)
        
        print(player)
        ch = input('card khod ra entekhab namayid: ')
        print(ch)
        zamine = ch.split(" ")[1]
        
        ## removing played card
        if zamine == 'del':
            player[0].remove(ch)
        elif zamine == 'pik':
            player[1].remove(ch)
        elif zamine == 'gishniz':
            player[2].remove(ch)
        elif zamine == 'khesht':
            player[3].remove(ch)
            
        ## check who won the round
        winner = functions.checkWinRound(ch, choice1, choice2, choice3, zamine)
        print(winner)
        
        if winner == 1 or winner == 3:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
        print(team1, team2)  
         
           
    ## bot2
    elif winner == 3:
        zamine = random.choice(zamineha)
        print(zamine)
        
        [bot2, choice2] = functions.chooseCard(bot2, zamine)
        print('bot2 ', choice2)
        [bot3, choice3] = functions.chooseCard(bot3, zamine)
        print('bot3 ', choice3)
        
        print(player)
        ch = input('card khod ra entekhab namayid: ')
        print(ch)
        zamine = ch.split(" ")[1]
        
        ## removing played card
        if zamine == 'del':
            player[0].remove(ch)
        elif zamine == 'pik':
            player[1].remove(ch)
        elif zamine == 'gishniz':
            player[2].remove(ch)
        elif zamine == 'khesht':
            player[3].remove(ch)
        
        [bot1, choice1] = functions.chooseCard(bot1, zamine)
        print('bot1 ', choice1)
            
        ## check who won the round
        winner = functions.checkWinRound(ch, choice1, choice2, choice3, zamine)
        print(winner)
        
        if winner == 1 or winner == 3:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
        print(team1, team2)  
            
    ## bot3
    elif winner == 4:
        zamine = random.choice(zamineha)
        print(zamine)
            
        [bot3, choice3] = functions.chooseCard(bot3, zamine)
        print('bot3 ', choice3)
        
        print(player)
        ch = input('card khod ra entekhab namayid: ')
        print(ch)
        zamine = ch.split(" ")[1]
        
        ## removing played card
        if zamine == 'del':
            player[0].remove(ch)
        elif zamine == 'pik':
            player[1].remove(ch)
        elif zamine == 'gishniz':
            player[2].remove(ch)
        elif zamine == 'khesht':
            player[3].remove(ch)
        
        [bot1, choice1] = functions.chooseCard(bot1, zamine)
        print('bot1 ', choice1)
        [bot2, choice2] = functions.chooseCard(bot2, zamine)
        print('bot2 ', choice2)
          
        ## check who won the round
        winner = functions.checkWinRound(ch, choice1, choice2, choice3, zamine)
        print(winner)
        
        if winner == 1 or winner == 3:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
        print(team1, team2)
        
    print("*"*100)
    
    if team1 == 7 or team2 == 7:
        break
        


