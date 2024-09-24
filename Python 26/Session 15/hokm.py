import random
import functions

cards_del = []
cards_khesht = []
cards_pik = []
cards_gishniz = []

for i in range(2, 15):
    cards_del.append(i)
    cards_khesht.append(i)
    cards_pik.append(i)
    cards_gishniz.append(i)

hakem = random.randint(0, 3)

hokmOptions = ['del', 'gishniz', 'khesht', 'pik']

if hakem == 0:
    hokm = input('choose hokm: ')
else:
    hokm = random.choice(hokmOptions)
        
if hokm == 'del':
    cards_del = [i*10 for i in cards_del]
elif hokm == 'gishniz':
    cards_gishniz = [i*10 for i in cards_gishniz]
elif hokm == 'khesht':
    cards_khesht = [i*10 for i in cards_khesht]
elif hokm == 'pik':
    cards_pik = [i*10 for i in cards_pik]
    

for i in range(len(cards_del)):
    cards_del[i] = (str(cards_del[i]) + ' del')
    cards_khesht[i] = (str(cards_khesht[i]) + ' khesht')
    cards_pik[i] = (str(cards_pik[i]) + ' pik')
    cards_gishniz[i] = (str(cards_gishniz[i]) + ' gishniz')

player1 = []
bot1 = []
bot2 = []
bot3 = []

cards = [cards_del, cards_khesht, cards_pik, cards_gishniz]
cards = [item for sublist in cards for item in sublist]


cards1 = []
for i in range(13):
    cards1.append(cards_del[i])
    cards1.append(cards_khesht[i])
    cards1.append(cards_pik[i])
    cards1.append(cards_gishniz[i])



for i in range(13):
    randomCard = random.choice(cards)
    player1.append(randomCard)
    cards.pop(cards.index(randomCard))
    
    randomCard = random.choice(cards)
    bot1.append(randomCard)
    cards.pop(cards.index(randomCard))
    
    randomCard = random.choice(cards)
    bot2.append(randomCard)
    cards.pop(cards.index(randomCard))
    
    randomCard = random.choice(cards)
    bot3.append(randomCard)
    cards.pop(cards.index(randomCard))
    

player1 = functions.golLength(player1)  
bot1 = functions.golLength(bot1)  
bot2 = functions.golLength(bot2)  
bot3 = functions.golLength(bot3)  

turn = hakem

print(hokm)

team1 = 0
team2 = 0

for i in range(13):
    if turn == 0:
        print(player1)
        p1 = input('choose a card: ')
        zamine = p1.split(' ')[1]
        print(p1) 
        
        b1 = functions.playGame(zamine, bot1)
        b2 = functions.playGame(zamine, bot2)
        b3 = functions.playGame(zamine, bot3)
        
        winner = functions.checkWinTurn(p1, b1, b2, b3, zamine)
        print(winner)
        if winner == 0 or winner == 2:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
        turn = 1
                
    # elif turn == 1:
    #     b1 = random.choice(bot1)
    #     zamine = b1.split(' ')[1] 
    #     print(zamine)
    # elif turn == 2:
    #     b2 = random.choice(bot2)
    #     zamine = b2.split(' ')[1] 
    #     print(zamine)
    # elif turn == 3:
    #     b3 = random.choice(bot3)
    #     zamine = b3.split(' ')[1] 
    #     print(zamine)
        
        
    
        
    
        
    
    
    


