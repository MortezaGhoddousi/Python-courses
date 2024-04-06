fname = 'Morteza'
age = 30
height = 1.86
isMale = True

myInfo = [fname, age, height, 91, isMale]

print(myInfo)
print(myInfo[1])
myInfo.append('Vollyball player')
print(myInfo)

if age > 18:
    print('Adult')
elif age < 10:
    print('Child')
else:
    print('Teenager')
    
for i in myInfo:
    print(i)
    
# [0, 1, 2, 3]
for i in range(4):
    print(i)
    
    
scores = []

for i in range(3):
    x = int(input('Enter your score: '))
    scores.append(x)
    print(scores)

sum = scores[0]+scores[1]+scores[2]
print(sum)