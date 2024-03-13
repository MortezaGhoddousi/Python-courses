# score1 = float(input('First score: '))
# score2 = float(input('Second score: '))
# score3 = float(input('Third score: '))
# score4 = float(input('Forth score: '))
# score5 = float(input('Fifth score: '))
# score6 = float(input('Sixth score: '))
# score7 = float(input('Seventh score: '))
# score8 = float(input('Eighth score: '))
# score9 = float(input('Ninth score: '))
# score10 = float(input('Tenth score: '))

# sum = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
# avg = sum/10
# print(f'The average is: {avg}')

sum = 0
for i in range(10):
    score = float(input(f"Enter your {i+1}th score: "))
    sum = sum + score   
avg = sum/10
print(f'The average is: {avg}')
