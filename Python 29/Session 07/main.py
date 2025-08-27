Info = ["Morteza", "Ghoddousi", 31, 1.85, 83, True, ['VolleyBall', 'Programming', 'Movies']]

print(f'First name: {Info[0]}')
print(f'Last name: {Info[1]}')
print(f'Age: {Info[2]}')
print(f'Height: {Info[3]}')
print(f'Weight: {Info[4]}')
print(f'Male: {Info[5]}')
print(f'Hobbies: {Info[6]}')

print(Info[6][1])

# Dictionaries
MyInfo = {
          'firstName': 'Morteza',
          'lastName': 'Ghoddousi',
          'age': 31,
          'height': 1.85,
          'weight': 83,
          'male': True,
          'hobbies': ['VolleyBall', 'Programming', 'Movies']
        }

print(MyInfo['firstName'])
print(MyInfo.get('firstName'))
print(MyInfo.keys())
print(MyInfo.values())


for i in MyInfo.values():
    print(i)

for i in Info:
    print(i)


from random import randint, random, choice

print(randint(2, 8))
print(random())

options = ['Morteza', 'AmirAli', 'Mohammad']
print(choice(options))

from datetime import datetime
print(datetime.now())

from time import sleep

print('start sleeping')
sleep(2)
print('end of sleeping')

import os

os.mkdir('C:/Users/hp/Desktop/Python-courses/Python 29/Session 07/operating system')

os.rmdir('C:/Users/hp/Desktop/Python-courses/Python 29/Session 07/operating system')

# sleep(5)
# os.system("shutdown /l")
