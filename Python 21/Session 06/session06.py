num_stu = int(input('Enter the number of your students: '))

for student in range(num_stu):
    # score = int(input('Enter the score of' +  str(student+1) + 'th student: '))
    score = int(input(f'Enter the score of {student+1}th student: '))
    while score<0 or score>20:
        print('Invalid input')
        score = int(input(f'Enter the score of {student+1}th student again: '))
    if score >= 10:
        print(f'{student+1}th student passed')
    else:
        print(f'{student+1}th student failed')