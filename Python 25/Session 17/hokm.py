import random
import functions

cards = range(2, 15)
delCards = []
gishnizCards = []
kheshtCards = []
pikCards = []

for i in cards:
    delCards.append(str(i)+' del')
    gishnizCards.append(str(i)+' gishniz')
    kheshtCards.append(str(i)+' khesht')
    pikCards.append(str(i)+' pik')
    
    
# hakem = random.randint(0, 3)
hakem = 0

hokm = functions.defHokm(hakem)

for i in range(13):
    if hokm == 'del':   
        splitted = delCards[i].split(' ')
        delCards[i] = str(int(splitted[0])*100) +  ' ' +splitted[1]
    elif hokm == 'gishniz':   
        splitted = gishnizCards[i].split(' ')
        gishnizCards[i] = str(int(splitted[0])*100) +  ' ' +splitted[1]
    elif hokm == 'khesht':   
        splitted = kheshtCards[i].split(' ')
        kheshtCards[i] = str(int(splitted[0])*100) +  ' ' +splitted[1]
    elif hokm == 'pik':   
        splitted = pikCards[i].split(' ')
        pikCards[i] = str(int(splitted[0])*100) +  ' ' +splitted[1]
        
player = []
bot1 = []
bot2 =[]
bot3 = []

allCards = []

for i in range(13):
    allCards.append(delCards[i])
    allCards.append(gishnizCards[i])
    allCards.append(kheshtCards[i])
    allCards.append(pikCards[i])
    
for i in range(13):
    card = random.choice(allCards)
    player.append(card)
    allCards.pop(allCards.index(card))
    
    card = random.choice(allCards)
    bot1.append(card)
    allCards.pop(allCards.index(card))
    
    card = random.choice(allCards)
    bot2.append(card)
    allCards.pop(allCards.index(card))
    
    card = random.choice(allCards)
    bot3.append(card)
    allCards.pop(allCards.index(card))
    
player = functions.classificationCards(player)    
bot1 = functions.classificationCards(bot1)    
bot2 = functions.classificationCards(bot2)    
bot3 = functions.classificationCards(bot3)    

turn = hakem

team1 = 0
team2 = 0

for i in range(13):
    if turn == 0:
        print(player)
        p1 = input('card khod ra entekhab konid: ')
        print(p1)
        player = functions.deleteCard(player, p1)
        zamine = p1.split(' ')[1]
        
        [b1, bot1] = functions.playGame(bot1, zamine)
        [b2, bot2] = functions.playGame(bot2, zamine)
        [b3, bot3] = functions.playGame(bot3, zamine)
        
        winner = functions.checkWin(p1, b1, b2, b3, zamine)
        turn = winner
        
        if winner == 0 or winner == 2:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
        
        print('winner: ', winner)
        print('Team1: ', team1)
        print('Team2: ', team2)
        
    if turn == 1:
        
        r = random.randint(0, 3)
        while len(bot1[r]) == 0:
            r = random.randint(0, 3)
        if r == 0:
            zamine = 'del'
        if r == 1:
            zamine = 'gishniz'
        if r == 2:
            zamine = 'khesht'
        if r == 3:
            zamine = 'pik'
                     
        [b1, bot1] = functions.playGame(bot1, zamine)
        [b2, bot2] = functions.playGame(bot2, zamine)
        [b3, bot3] = functions.playGame(bot3, zamine)
        
        print(player)
        p1 = input('card khod ra entekhab konid: ')
        player = functions.deleteCard(player, p1)
        print(p1)
     
        winner = functions.checkWin(p1, b1, b2, b3, zamine)
        
        if winner == 0 or winner == 2:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
        
        turn = winner
        print('winner: ', winner)
        print('Team1: ', team1)
        print('Team2: ', team2)
        
    if turn == 2:
        
        r = random.randint(0, 3)
        while len(bot2[r]) == 0:
            r = random.randint(0, 3)
        if r == 0:
            zamine = 'del'
        if r == 1:
            zamine = 'gishniz'
        if r == 2:
            zamine = 'khesht'
        if r == 3:
            zamine = 'pik'
                     
        [b2, bot2] = functions.playGame(bot2, zamine)
        [b3, bot3] = functions.playGame(bot3, zamine)
        
        print(player)
        p1 = input('card khod ra entekhab konid: ')
        player = functions.deleteCard(player, p1)
        print(p1)
     
        [b1, bot1] = functions.playGame(bot1, zamine)
        
        winner = functions.checkWin(p1, b1, b2, b3, zamine)
        
        if winner == 0 or winner == 2:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
            
        turn = winner
        print('winner: ', winner)
        print('Team1: ', team1)
        print('Team2: ', team2)
        
    if turn == 3:
        
        r = random.randint(0, 3)
        while len(bot3[r]) == 0:
            r = random.randint(0, 3)
        if r == 0:
            zamine = 'del'
        if r == 1:
            zamine = 'gishniz'
        if r == 2:
            zamine = 'khesht'
        if r == 3:
            zamine = 'pik'
                     
        [b3, bot3] = functions.playGame(bot3, zamine)
        
        print(player)
        p1 = input('card khod ra entekhab konid: ')
        player = functions.deleteCard(player, p1)
        print(p1)
     
        [b1, bot1] = functions.playGame(bot1, zamine)
        [b2, bot2] = functions.playGame(bot2, zamine)
        
        winner = functions.checkWin(p1, b1, b2, b3, zamine)
        
        if winner == 0 or winner == 2:
            team1 = team1 + 1
        else:
            team2 = team2 + 1
            
            
        turn = winner
        print('winner: ', winner)
        print('Team1: ', team1)
        print('Team2: ', team2)

print('Team1: ', team1)
print('Team2: ', team2)
