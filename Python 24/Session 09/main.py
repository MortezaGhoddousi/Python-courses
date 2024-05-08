names = ['Morteza', 'Mahtab'.upper(), 'Moslem', 'Hossein', 'Mohammad']
print(names)
names.insert(2, 'Iman'.lower())
print(names)

names.pop(4)
print(names)

names.pop(names.index('Moslem'))
print(names)

print('ghoddousi'.find('o'))

inds = []

string = 'ghoddousi'
for i in range(len(string)):
    if string[i] == 'o':
        inds.append(i)
        
print(inds)

inds = []
for i, l in enumerate(string):
    if l == 'o':
        inds.append(i)
        
print(inds)
    


# print(len(names))

# for i in range(len(names)):
#     print('hello')
    
# print(names.index('Mahtab'))


# names = []

# for i in range(4):
#     x = input('Enter your name: ')
#     names.append(x)
#     print(names)

def f(x):
    y = 2*x + 3
    print(y)
    # return y
    



y = f(5)
print(y)

y = f(9)
print(y)
