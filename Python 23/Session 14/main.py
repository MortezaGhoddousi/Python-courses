# num_stu = int(input('Enter the number of your students: '))

# nums = []
# i = 0
# Min = 21
# Max = -1
# Sum = 0

# while i < num_stu:
#     nums.append(float(input("Enter the score: ")))
#     print(nums)

#     if nums[-1] < Min:
#         Min = nums[-1]
    
#     if nums[-1] > Max:
#         Max = nums[-1]

#     Sum = Sum + nums[-1]

#     i = i+1

# avg = Sum/num_stu

# print(Min, Max, avg)

# print(nums)

# import numpy
# import matplotlib.pyplot as plt

# num_stu = int(input('Enter the number of your students: '))

# nums = []
# i = 0

# while i < num_stu:
#     nums.append(float(input("Enter the score: ")))
#     print(nums)
#     i = i+1

# Min = numpy.amin(nums)
# Max = numpy.amax(nums)
# avg = numpy.average(nums)
# print(Min, Max, avg)

# print(nums)

# plt.figure()
# # plt.plot(nums)
# plt.scatter(range(1, num_stu+1), nums)
# plt.grid()
# plt.title('The scores of students')
# plt.xlabel('Students')
# plt.ylabel('Scores')
# plt.show()

num = int(input('Enter the number: '))

i = 1
even = 0

while i <= num:
    if i%2 == 0:
        even = even+1
    i = i+1

print(even)