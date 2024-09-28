import random
import numpy as np

def defHokm(hakem):
    if hakem == 0:
        hokm = input('hokm ra vared konid: ')
    else:
        r = random.randint(0, 3)
        if r == 0:
            hokm = 'del'
        elif r == 1:
            hokm = 'gishniz'
        elif r == 2:
            hokm = 'khesht'
        elif r == 3:
            hokm = 'pik'
        
    print('hokm: ', hokm)
    return hokm

def classificationCards (cards):
    delCards = []
    gishnizCards = []
    kheshtCards = []
    pikCards = []
    for i in cards:
        card = i.split(' ')
        if card[1] == 'del':
            delCards.append(i)
        elif card[1] == 'gishniz':
            gishnizCards.append(i)
        elif card[1] == 'khesht':
            kheshtCards.append(i)
        elif card[1] == 'pik':
            pikCards.append(i)
    return [delCards, gishnizCards, kheshtCards, pikCards]

def playGame(cards, zamine):
    if zamine == 'del':
        if len(cards[0]) > 0:
            b = random.choice(cards[0])
            print(b)
            cards[0].pop(cards[0].index(b))
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b = random.choice(cards[r])
            print(b)
            cards[r].pop(cards[r].index(b))
    elif zamine == 'gishniz':
        if len(cards[1]) > 0:
            b = random.choice(cards[1])
            print(b)
            cards[1].pop(cards[1].index(b))
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b = random.choice(cards[r])
            print(b)
            cards[r].pop(cards[r].index(b))
    elif zamine == 'khesht':
        if len(cards[2]) > 0:
            b = random.choice(cards[2])
            print(b)
            cards[2].pop(cards[2].index(b))
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b = random.choice(cards[r])
            print(b)
            cards[r].pop(cards[r].index(b))
    elif zamine == 'pik':
        if len(cards[3]) > 0:
            b = random.choice(cards[3])
            print(b)
            cards[3].pop(cards[3].index(b))
        else:
            r = random.randint(0, 3)
            while len(cards[r]) == 0:
                r = random.randint(0, 3)
            b = random.choice(cards[r])
            print(b)
            cards[r].pop(cards[r].index(b))
    return [b, cards]

def checkWin(p1, b1, b2, b3, zamine):
    p1 = p1.split(' ')
    b1 = b1.split(' ')
    b2 = b2.split(' ')
    b3 = b3.split(' ')
    if p1[1] != zamine:
        p1[0] = float(p1[0]) / 10
    if b1[1] != zamine:
        b1[0] = float(b1[0]) / 10
    if b2[1] != zamine:
        b2[0] = float(b2[0]) / 10
    if b3[1] != zamine:
        b3[0] = float(b3[0]) / 10
        
    return np.argmax([float(p1[0]), float(b1[0]), float(b2[0]), float(b3[0])])
    
            
def deleteCard (cards, p):
    zamine = p.split(' ')[1]
    if zamine == 'del':
        cards[0].pop(cards[0].index(p))
    elif zamine == 'gishniz':
        cards[1].pop(cards[1].index(p))
    elif zamine == 'khesht':
        cards[2].pop(cards[2].index(p))
    elif zamine == 'pik':
        cards[3].pop(cards[3].index(p))
    return cards