myList = ['Amir', 'Mahla', 'Morteza']
print(myList[0])

myList[1] = 'Razzaghi'
print(myList)

print(len(myList))

myTuple = ('Amir', 'Mahla', 'Morteza')
print(myTuple[0])

# myTuple[1] = 'Razzaghi'
# print(myTuple)

print(len(myTuple))

myDictionary = {0: 'Amir', 1: 'Mahla', 2: 'Morteza'}
print(myDictionary[0])


myInfoDic = {'fname': 'Morteza', 'lName': 'Ghoddousi', 'age': 30, 'weight': 90, 'height': 1.86}
print(myInfoDic['fname'])
print(myInfoDic.get('fName', 0))



print(myInfoDic['age'])

myInfoList = ['Morteza', 'Ghoddousi', 30, 90, 1.86]

Database = [{'fname': 'Morteza', 'lName': 'Ghoddousi', 'age': 30, 'weight': 90, 'height': 1.86}, 
            {'fname': 'Mahla', 'lName': 'Razzaghi', 'age': 21, 'weight': 60, 'height': 1.65}, 
            {'fname': 'Amir', 'lName': 'Cheraghi', 'age': 35, 'weight': 74, 'height': 1.77}]

print(Database[0]['fname'], Database[0]['lName'])

print(Database[0].get('fName', 'unknown'))


# fname = input('enter your first name: ')
# lname = input('enter your last name: ')
# age = int(input('enter your age: '))
# weight = int(input('enter your weight: '))
# height = float(input('enter your height: '))

# newStudent = {'fname': fname, 'lName': lname, 'age': age, 'weight': weight, 'height': height}

# Database.append(newStudent)

# print(Database)

Database[1]['age'] = 22
# print(Database)

mySet = {20, 40, 'Morteza', 40, 51}
print(mySet)

cubes = [i**3 for i in range(5)]
print(cubes)

Cubes = []
for i in range(5):
    Cubes.append(i**3)
    
print(Cubes)


cubes = [i**3 for i in range(5) if i%2==0]
print(cubes)

Cubes = []
for i in range(5):
    if i%2==0:
        Cubes.append(i**3)
    
print(Cubes)

print((lambda x, y: 2*x+y)(2, 3))




