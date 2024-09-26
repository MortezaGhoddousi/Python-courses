import random
import numpy as np

def golLength(cards):
    
    delCards = []
    gishnizCards = []
    kheshtCards = []
    pikCards = []
     
    for card in cards:
        gol = card.split(' ')[1] 
        if gol == 'del':
            delCards.append(card)
        elif gol == 'gishniz':
            gishnizCards.append(card) 
        elif gol == 'khesht':
            kheshtCards.append(card)
        elif gol == 'pik':
            pikCards.append(card)
            
    return [delCards, gishnizCards, kheshtCards, pikCards]

def playGame (zamine, cards):
    if zamine == 'del':
        if len(cards[0]) > 0:
            b1 = random.choice(cards[0])
            cards[0].pop(cards[0].index(b1))
            print(b1) 
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b1 = random.choice(cards[r])
            cards[r].pop(cards[r].index(b1))
            print(b1)
    if zamine == 'gishniz':
        if len(cards[1]) > 0:
            b1 = random.choice(cards[1])
            cards[1].pop(cards[1].index(b1))
            print(b1) 
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b1 = random.choice(cards[r])
            cards[r].pop(cards[r].index(b1))
            print(b1)
    if zamine == 'khesht':
        if len(cards[2]) > 0:
            b1 = random.choice(cards[2])
            cards[2].pop(cards[2].index(b1))
            print(b1) 
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b1 = random.choice(cards[r])
            cards[r].pop(cards[r].index(b1))
            print(b1)             
    if zamine == 'pik':
        if len(cards[3]) > 0:
            b1 = random.choice(cards[3])
            cards[3].pop(cards[3].index(b1))
            print(b1) 
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b1 = random.choice(cards[r])
            cards[r].pop(cards[r].index(b1))
            print(b1)
    return [b1, cards]
            
def checkWinTurn(player1, bot1, bot2, bot3, zamine):
    p1 = player1.split(' ')
    b1 = bot1.split(' ')
    b2 = bot2.split(' ')
    b3 = bot3.split(' ')
    
    if p1[1] != zamine:
        p1[0] = str(int(p1[0])/10)
    if b1[1] != zamine:
        b1[0] = str(int(b1[0])/10)
    if b2[1] != zamine:
        b2[0] = str(int(b2[0])/10)
    if b3[1] != zamine:
        b3[0] = str(int(b3[0])/10)
    
    return np.argmax([float(p1[0]), float(b1[0]), float(b2[0]), float(b3[0])])
    