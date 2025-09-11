# # List 

name1 = 'Soroosh'
name2 = 'Kian'
name3 = 'Arman'
name4 = 'Morteza'

print(name1)
print(name2)
print(name3)
print(name4)

names = ['Soroosh', 'Kian', 'Arman', 'Morteza']

print(names)
print(names[3])

info = ['Morteza', 'Ghoddousi', 31, 83, 1.86, True, ['Programming languages', 'Volleyball']]

print(info[6][1])

print(info)
info.append(False)
print(info)

info.insert(2, 'Teacher')
print(info)

info.pop(8)
print(info)

print(info.index(1.86))

print(len(info))

# newList = [info[0], info[1]]

newList = info[0:2]
print(newList)

print(info[2:7])
print(info[0: 4])
print(info[:4])
print(info[7])

print(info[5:8])
print(info[5:])
print(info[:])
print(info[len(info)-1])

print(info[-1])

print(info[6])
print(info[-2])

info.reverse()
print(info)

# newNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newNumber = range(0, 10)

print(newNumber)

# # For loop

# for variable in list:
#     body

newNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in newNumber:
    print(i)

for i in range(10):
    print('hello')


for i in info:
    print(i)