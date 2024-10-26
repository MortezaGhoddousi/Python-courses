myLi = ['Morteza', 'ghoddousi', 30, 1.85, 92, True]

print(myLi)
myLi[2] = 31
print(myLi)


myTuple = ('Morteza', 'ghoddousi', 30, 1.85, 92, True)
print(myTuple)

myDict = {'fname': 'Morteza', "lname":'Ghoddousi', 'age':30, 'height': 1.85, 'weight': 92, 'isMale': True}

print(myDict)
myDict['age'] = '31'
print(myDict)

print('isMale' in myDict)
print('ismale' in myDict)

Mat = [['a', 'b', 'c', 'd'], 
       ['e', 'f', 'g', 'h'], 
       ['i', 'j', 'k', 'l'], 
       ['m', 'n', 'o', 'p']]

print(Mat[1][1])

Mat[1][2] = 'z'
print(Mat[1][2])

import numpy as np

scores = [[18, 17, 7, 19.5, 20, 18], 
          [4.25, 7, 11, 9.75, 9.75, 1], 
          [15, 14, 19, 18, 17, 13], 
          [14, 14, 15, 16, 18, 20], 
          [12, 13, 17, 9.75, 10, 12]] 

print('Riazi mohandesi:', scores[1][-1])

newScores = {
    'AmirReza': [18, 17, 7, 19.5, 20, 18],
    'Setayesh': [4.25, 7, 11, 9.75, 9.75, 1],
    'Nazanin': [15, 14, 19, 18, 17, 13],
    'Matin': [14, 14, 15, 16, 18, 20],
    'Morteza': [12, 13, 17, 9.75, 10, 12]
}

print('Riazi mohandesi:', newScores['Setayesh'][-1])

npScores = np.array([[18, 17, 7, 19.5, 20, 18], 
                     [4.25, 7, 11, 9.75, 9.75, 1], 
                     [15, 14, 19, 18, 17, 13], 
                     [14, 14, 15, 16, 18, 20], 
                     [12, 13, 17, 9.75, 10, 12]])

print('Riazi mohandesi:', npScores[1][-1])

