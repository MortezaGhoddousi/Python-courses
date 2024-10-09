myList = []

for i in range(5):
    if i != 2:
        myList.append(i**2)
    
print(myList)

myNewList = [i**2 for i in range(5) if i!=2]
print(myNewList)

mySet = {1, 2, 3, 4, 5}

print(1 in mySet)

# print(mySet.get(1))

def sumTwo(x):
    return x + 2

print(sumTwo(5))

print((lambda x: x+2)(5))


x = range(11)

y = []
for i in x:
    y.append(i+3)
    
print(y)

def addThree(x):
    return x+3

print(list(map(addThree, x)))

def isEven(x):
    return x%2 == 0

print(list(filter(isEven, x)))

print(list(filter((lambda x: x%2==0), x)))
