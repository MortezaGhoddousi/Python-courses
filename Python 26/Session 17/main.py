# myDictanary = {
#                'fname': 'Morteza', 
#                'lname': 'Ghoddousi', 
#                'age': 30,
#                'gender': 'Male',
#                'height': 1.86,
#                'weight': 92
#                }


# print(myDictanary.get('fname', 'Not Found'))
# print(myDictanary.get('Fname', 'Not Found'))



# print(myDictanary['fname'])
# # print(myDictanary['Fname'])
# print(myDictanary['lname'])
# print(myDictanary['age'])
# print(myDictanary['gender'])
# print(myDictanary['height'])
# print(myDictanary['weight'])

# myList = ['M', 'GH']
# print(myList)
# myList[0] = 'A'
# print(myList)

# myTuple = ('M', 'GH')
# print(myTuple)
# # myTuple[0] = 'A'
# # print(myTuple)

# myString = 'MGH'
# print(myString)
# # myString[0] = 'A'
# # print(myString)

# nums = {
# 1: "one",
# 2: "two",
# 3: "three",
# }
# print(1 in nums)
# print("three" in nums)
# print(4 not in nums)

# tuple = (1, (1, 2, 3))
# print(tuple[1][1])

import functions
k = 2

plainText = 'sayhello'

encryptedText = functions.encrypted(plainText, k)
print(encryptedText)

decryptedText = functions.decrypted(encryptedText, k)
print(decryptedText)

possibleAnswers = functions.brootforceAttack(encryptedText)

print('*'*20)
for A in possibleAnswers:
    print(A)

