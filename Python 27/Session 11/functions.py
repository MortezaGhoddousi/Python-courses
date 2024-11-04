import random
from numpy import argmax

def splitTheCards (allCards):
    player = []
    bot1 = []
    bot2 = []
    bot3 = []
    
    for i in range(13):
        card = random.choice(allCards)
        player.append(card)
        allCards.remove(card)
        
    for i in range(13):
        card = random.choice(allCards)
        bot1.append(card)
        allCards.remove(card)
        
    for i in range(13):
        card = random.choice(allCards)
        bot2.append(card)
        allCards.remove(card)
        
    for i in range(13):
        card = random.choice(allCards)
        bot3.append(card)
        allCards.remove(card)
        
    return [player, bot1, bot2, bot3]

def sortCards (cards):
    Del = []
    Pik = []
    Gishniz = []
    Khesht = []
    for i in cards:
        temp = i.split(" ")
        if temp[1] == 'del':
            Del.append(i)
        elif temp[1] == 'pik':
            Pik.append(i)
        elif temp[1] == 'gishniz':
            Gishniz.append(i)
        elif temp[1] == 'khesht':
            Khesht.append(i)
            
    return [Del, Pik, Gishniz, Khesht]   
        
def chooseCard(cards, zamine):
    if zamine == 'del':
        choice = random.choice(cards[0])
        cards[0].remove(choice)
    elif zamine == 'pik':
        choice = random.choice(cards[1])
        cards[1].remove(choice)
    elif zamine == 'gishniz':
        choice = random.choice(cards[2])
        cards[2].remove(choice)
    elif zamine == 'khesht':
        choice = random.choice(cards[3])
        cards[3].remove(choice)
    return cards, choice

def checkWinRound(p, b1, b2, b3):
    p = float(p.split(' ')[0])
    b1 = float(b1.split(' ')[0])
    b2 = float(b2.split(' ')[0])
    b3 = float(b3.split(' ')[0])
    
    return argmax([p, b1, b2, b3])+1
    
    