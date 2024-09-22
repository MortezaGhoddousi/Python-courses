import random

cards_del = range(2, 15)
cards_khesht = range(2, 15)
cards_pick = range(2, 15)
cards_gishniz = range(2, 15)

hakem = random.randint(1, 4)

if hakem == 1:
    hokm = input('choose hokm: ')

if hokm == 'del':
    cards_del = cards_del * 10
