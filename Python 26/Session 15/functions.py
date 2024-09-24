import random
import numpy as np

def golLength(cards):
    dell = 0
    gishniz = 0
    khesht = 0
    pik = 0
    
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
            print(b1) 
        else:
            r = random.randint(1, 3)
            b1 = random.choice(cards[r])
            print(b1)
    if zamine == 'gishniz':
        if len(cards[1]) > 0:
            b1 = random.choice(cards[1])
            print(b1) 
        else:
            r = random.randint(0, 3)
            while r != 1:
                r = random.randint(0, 3)
            b1 = random.choice(cards[r])
            print(b1)
    if zamine == 'khesht':
        if len(cards[2]) > 0:
            b1 = random.choice(cards[2])
            print(b1) 
        else:
            r = random.randint(0, 3)
            while r != 2:
                r = random.randint(0, 3)
            b1 = random.choice(cards[r])
            print(b1)             
    if zamine == 'pik':
        if len(cards[3]) > 0:
            b1 = random.choice(cards[3])
            print(b1) 
        else:
            r = random.randint(0, 3)
            while r != 3:
                r = random.randint(0, 3)
            b1 = random.choice(cards[r])
            print(b1)
    return b1
            
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
    
    return np.argmax([int(p1[0]), int(b1[0]), int(b2[0]), int(b3[0])])
    