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