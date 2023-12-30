import random
import numpy as np
# import pandas

   
num_stu = int(input('Enter the number of students: '))
i = 0
min_num = 21
max_num = -1

my_list = []

sum_ = 0

while i<num_stu:
    x = random.randint(0, 20)
    sum_ = sum_+x
    # my_list[i] = x
    my_list.append(x)
    # print(x)
    if x<min_num:
        min_num = x
        min_ind = i
    if x>max_num:
        max_num = x
        max_ind = i
    i = i+1
    
# sum_ = 0
# for score in my_list:
#     sum_ = sum_+score

average = sum_ / len(my_list)

sum_ = 0
for score in my_list:
    sum_ = sum_ + (score-average)**2

variance = sum_ / len(my_list)    


Max_ind = my_list.index(max_num)
Min_ind = my_list.index(min_num)
print(f'My list is: {my_list}')
print(f'Minimum number is: {min_num}')
print(f'Maximum number is: {max_num}')
print(f'Average of scores is: {average}')
print(f'Variance of scores is: {variance}')
print(f'Index of Minimum number is: {min_ind}')
print(f'Index of Maximum number is: {max_ind}')

print(f'Index of Minimum number is: {Min_ind}')
print(f'Index of Maximum number is: {Max_ind}')

print('------------------------------------------------------------')
print('numpy')

Min = np.min(my_list)
Max = np.max(my_list)
iMin = np.argmin(my_list)
iMax = np.argmax(my_list)
Variance = np.var(my_list)
Average = np.average(my_list)
SD = np.std(my_list)
sd = np.sqrt(Variance)

print(f'Minimum number is: {Min}')
print(f'Maximum number is: {Max}')
print(f'Index of Minimum number is: {iMin}')
print(f'Index of Maximum number is: {iMax}')
print(f'Average of scores is: {Average}')
print(f'Variance of scores is: {Variance}')
print(f'Standard deviation of scores is: {SD}')
print(f'Standard deviation of scores is: {sd}')
