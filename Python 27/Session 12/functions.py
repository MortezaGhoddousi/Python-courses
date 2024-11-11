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

def sortCards (cards, hokm):
    
    zamineha = ['del', 'pik', 'gishniz', 'khesht']
    ind = zamineha.index(hokm)
    
    Del = []
    Pik = []
    Gishniz = []
    Khesht = []
    
    for i in cards:
        temp = i.split(" ")
        if temp[1] == 'del':
            if ind == 0:
                Del.append(str(float(temp[0])*100)+' del')
            else:
                Del.append(i)
        elif temp[1] == 'pik':
            if ind == 1:
                Pik.append(str(float(temp[0])*100)+' pik')
            else:
                Pik.append(i)
          
        elif temp[1] == 'gishniz':
            if ind == 2:
                Gishniz.append(str(float(temp[0])*100)+' gishniz')
            else:
                Gishniz.append(i)
        elif temp[1] == 'khesht':
            if ind == 3:
                Khesht.append(str(float(temp[0])*100)+' khesht')
            else:
                Khesht.append(i)
            
    return [Del, Pik, Gishniz, Khesht]   
        
def chooseCard(cards, zamine):
    if zamine == 'del':
        if len(cards[0])>0:
            choice = random.choice(cards[0])
            cards[0].remove(choice)
        else:
            while True:
                ind = random.randint(1, 3)
                if len(cards[ind])!=0:
                    break
            choice = random.choice(cards[ind])
            cards[ind].remove(choice)
                
    elif zamine == 'pik':
        if len(cards[1])>0:
            choice = random.choice(cards[1])
            cards[1].remove(choice)
        else:
            while True:
                ran = [0, 2, 3]
                ind = random.choice(ran)
                if len(cards[ind])!=0:
                    break
            choice = random.choice(cards[ind])
            cards[ind].remove(choice)
            
    elif zamine == 'gishniz':
        if len(cards[2])>0:
            choice = random.choice(cards[2])
            cards[2].remove(choice)
        else:
            while True:
                ran = [0, 1, 3]
                ind = random.choice(ran)
                if len(cards[ind])!=0:
                    break
            choice = random.choice(cards[ind])
            cards[ind].remove(choice)
    elif zamine == 'khesht':
        if len(cards[3])>0:
            choice = random.choice(cards[3])
            cards[3].remove(choice)
        else:
            while True:
                ind = random.randint(0, 2)
                if len(cards[ind])!=0:
                    break
            choice = random.choice(cards[ind])
            cards[ind].remove(choice)
    return cards, choice

def checkWinRound(p, b1, b2, b3, zamine):
    
    p = p.split(' ')
    if p[1] != zamine:
        p[0] = float(p[0])/10
        
    b1 = b1.split(' ')
    if b1[1] != zamine:
        b1[0] = float(b1[0])/10
        
    b2 = b2.split(' ')
    if b2[1] != zamine:
        b2[0] = float(b2[0])/10
        
    b3 = b3.split(' ')
    if b3[1] != zamine:
        b3[0] = float(b3[0])/10
   
    return argmax([float(p[0]), float(b1[0]), float(b2[0]), float(b3[0])])+1
    
    