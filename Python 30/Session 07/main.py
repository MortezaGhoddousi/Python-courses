# List

myList = ['Morteza', 'Ghoddousi', 31, 1.86, 83, True]
print(myList[0])

print(myList)
myList[2] = 32
print(myList)

# Tuple
myTuple = ('Morteza', 'Ghoddousi', 31, 1.86, 83, True)

print(myTuple[0])
print(myTuple)
# myTuple[2] = 32
# print(myTuple)

# Dictionary
myDict = {
    "firstName": "Morteza",
    "lastName": "Ghoddousi",
    "age": 31,
    "height": 1.86,
    "weight": 83,
    "isMale": True
    }

print(myDict["firstName"])
print(myDict.get('FirstName', "no key"))

print(myDict)

print(myDict.keys())
print(myDict.values())

for i in myList:
    print(i)

for i in myTuple:
    print(i)

for i in myDict.values():
    print(i)

# Set
mySet = {'Morteza', 'Ghoddousi', 31, 1.86, 83, True, "Morteza"}

print(mySet)

mySet.add('Programming')
mySet.add('Volleyball')
mySet.add(31)

print(mySet)

newSet = mySet.difference({'Morteza', 'Ghoddousi'})

print(newSet)

# mySet.difference_update({'Morteza', 'Ghoddousi'})
print(mySet)

mySet.discard(33)
mySet.remove(31)
print(mySet)

print({'Morteza', 'Ghoddousi'}.issubset(mySet))


# matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
print(x)
print(x.shape)

y = [np.sin(i) for i in x]

# y = []
# for i in x:
#     y.append(np.sin(i))

# print(y)

# for i in x:
#     print(i)

plt.figure()

plt.plot(x, y, color='r', alpha=0.5, linewidth=3, marker='*')
plt.title('Sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()


plt.show()

# exercise

x = np.linspace(-2, 2, 50)
y = [i**2+3 for i in x]
y1 = [i**2 for i in x]

plt.figure()
plt.title('f(x) = x^2 + 3')
plt.xlabel('X')
plt.ylabel('Y')

plt.grid()
plt.plot(x, y, linewidth=2, label='x^2+3')
plt.plot(x, y1, linewidth=2, label='x^2')

plt.legend()

plt.show()

