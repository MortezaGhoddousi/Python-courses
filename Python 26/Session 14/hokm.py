import random

cards_del = []
cards_khesht = []
cards_pik = []
cards_gishniz = []

for i in range(2, 15):
    cards_del.append(i)
    cards_khesht.append(i)
    cards_pik.append(i)
    cards_gishniz.append(i)

hakem = random.randint(1, 4)

hokmOptions = ['del', 'gishniz', 'khesht', 'pik']

if hakem == 1:
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
    print(cards)
    
    randomCard = random.choice(cards)
    bot1.append(randomCard)
    cards.pop(cards.index(randomCard))
    print(cards)
    
    randomCard = random.choice(cards)
    bot2.append(randomCard)
    cards.pop(cards.index(randomCard))
    print(cards)
    
    randomCard = random.choice(cards)
    bot3.append(randomCard)
    cards.pop(cards.index(randomCard))
    print(cards)
    
print(player1)
print(bot1)
print(bot2)
print(bot3)
  
        
