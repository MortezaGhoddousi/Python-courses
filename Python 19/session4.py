# seats = 20

# while seats>0:  
#     # print("Ticket sold")
#     seats = seats-1
#     print(seats>0)

# print("Maximum capacity")

# Password = input("Please set your password: ")

# print("Welcome to this app")

# guess = input("Enter your password: ")

# # while guess != Password:
# #     print("Password is incorrect!")
# #     guess = input("Enter your password: ")

# if guess == Password:
#     print("Logged in from if statement!")
# else:
#     print("Password is incorrect! ")
#     print("Logged off")


# age = int(input("Enter your age: "))

# if age < 10:
#     print("Child")
# elif age >= 10 and age < 20:
#     print("Teenager")
# elif age >=20 and age < 50:
#     print("Adult")
# else:
#     print("Elderly")

# num_stu = int(input("Enter the number of your student: "))

# scores = []
# min = 21
# max = -1
# sum = 0
# for i in range(num_stu):
#     x = float(input(f"Enter {i+1}th student's score: "))
#     scores.append(x)
#     if x > max:
#         max = x
#     if x < min:
#         min = x
#     sum = sum+x

# avg = sum/num_stu
# print(f"Average your students' score is: {avg}")
# print(f"Maximum score of your students is: {max}")
# print(f"Minimum score of your students is: {min}")

import numpy

num_stu = int(input("Enter the number of your student: "))
scores = []   
for i in range(num_stu):
    x = float(input(f"Enter {i+1}th student's score: "))
    scores.append(x)

Min = numpy.min(scores)
Max = numpy.max(scores)
avg = numpy.average(scores)
var = numpy.var(scores)
ind = numpy.argmax(scores)
print(ind)

print(f"Maximum score of your students is: {Max}")
print(f"Minimum score of your students is: {Min}")
print(f"Average your students' score is: {avg}")
print(f"Varience of your students is: {var}")








