i = 0
while i<4:
    print (i)
    i = i+1

age = 16

if age > 18:
    print('Adult')
elif age > 10 and age < 18:
    print('Teenager')
else:
    print('Child')

inf = ['Morteza', 'Ghoddousi', 30, 'Male', 1.86, 91]
print(inf)
inf[5] = 92
print(inf)


cart = ["milk", "eggs", "apples"]

print(cart[2])


for i in "Morteza":
    print(i)


inf = ['Morteza', 'Ghoddousi', 30, 'Male', 1.86, 91]

newinf = inf[0:2]
print(newinf)
print(inf[:2])

print(inf[2:5])

print(inf[3:6])
print(inf[3:])
print(inf[:])

print(inf[5])
print(inf[-1])

print(inf[3])
print(inf[-3])

print(inf[3:6])
print(inf[3:])
print(inf[-3:0])
