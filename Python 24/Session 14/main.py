n = [2, 4, 6, 8]
res = 1

n[2] = 9

for x in n[1:3]:
    res = res*x
    
print(res)

dic = {
    0: 'Morteza',
    3: 'Ghoddousi',
    'age': 30,    
}

x = 4
y = 5

[x, y] = [4, 5]
print(x, y)

x, y = (5, 9)
print(x, y)

print(dic[0])
print(dic['age'])

print(1 in dic)

print(dic[0])
print(dic.get(0))

# print(dic[1])
print(dic.get(1, 'not found'))

print(len(dic))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

data = {
'Singapore': 1,
'Ireland': 6,
'United Kingdom': 7,
'Germany': 27,
'Armenia': 34,
'United States': 17,
'Canada': 9,
'Italy': 74
}

# country = input('Enter the name of country: ').split(' ')

# events1 = []
# for c in country:
#     events1.append(c.capitalize())
    
    
# events2 = [c.capitalize() for c in country]

# country = ' '.join(events2)

# print(data.get(country, 'Not found'))

# try:
#     print(data[country])
# except:
#     print('Not found')
    

# tuple = (1, (1, 2, 3))
# print(tuple[1])

contacts = [
('James', 42),
('Amy', 24),
('John', 31),
('Amanda', 63),
('Bob', 18)
]

# name = input('Enter the name: ').capitalize()

# for i in contacts: 
#     if i[0] == name:
#         print(f'{name} is {i[1]}')


*a, b = [4, 8, 6, 7, 9, 11, 15]

print(a)
print(b)

def square(x=0, *y):
    print(x, y)
    
square(2, 4)

# square(2)

square(2, 4, 8, 9)

