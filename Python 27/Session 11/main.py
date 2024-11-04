import random
import functions

Del = range(2, 15)
Pik = range(2, 15)
Gishniz = range(2, 15)
Khesht = range(2, 15)

# DelCards = []
# for i in Del:
#     DelCards.append(str(i) + ' del')
    
DelCards = [str(i)+' del' for i in Del]
PikCards = [str(i)+' pik' for i in Pik]
GishnizCards = [str(i)+' gishniz' for i in Gishniz]
KheshtCards = [str(i)+' khesht' for i in Khesht]

# allCards = [DelCards, PikCards, GishnizCards, KheshtCards]

allCards = []

for i in range(13):
    allCards.append(DelCards[i])
    allCards.append(PikCards[i])
    allCards.append(GishnizCards[i])
    allCards.append(KheshtCards[i])
      
# print(allCards)

# hakem = random.randint(1, 4)
hakem = 1

zamineha = ['del', 'pik', 'gishniz', 'khesht']
if hakem == 1: 
    hokm = input('Hokm ra entekhab kon: ')
else:
    hokm = random.choice(zamineha)
  

[player, bot1, bot2, bot3] = functions.splitTheCards(allCards)

player = functions.sortCards(player)
bot1 = functions.sortCards(bot1)
bot2 = functions.sortCards(bot2)
bot3 = functions.sortCards(bot3)


winner = hakem

team1 = 0
team2 = 0

for r in range(13):
    if winner == 1:
        print(player)
        ch = input('card khod ra entekhab namayid: ')
        print(ch)
        zamine = ch.split(" ")[1]
        
        if zamine == 'del':
            player[0].remove(ch)
        elif zamine == 'pik':
            player[1].remove(ch)
        elif zamine == 'gishniz':
            player[2].remove(ch)
        elif zamine == 'khesht':
            player[3].remove(ch)
            
     
        [bot1, choice1] = functions.chooseCard(bot1, zamine)
        print(choice1)
        [bot2, choice2] = functions.chooseCard(bot2, zamine)
        print(choice2)
        [bot3, choice3] = functions.chooseCard(bot3, zamine)
        print(choice3)
        
        winner = functions.checkWinRound(ch, choice1, choice2, choice3)
        if winner == 1 or winner == 3:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
            
        
    
    else:
        pass
        



