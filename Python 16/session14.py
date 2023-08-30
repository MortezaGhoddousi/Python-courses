import numpy as np

number_of_courses = int(input("Enter the number of courses= "))
number_of_students = int(input("Enter the number of students= "))

average_student = []
for i in range(number_of_students):
    scores = []
    for j in range(number_of_courses):
        scores.append(float(input(f"Enter the {j+1}th score of {i+1}th student= ")))
    average_student.append(np.average(scores))
    print(average_student)

print(np.max(average_student))
print(np.min(average_student))


x = int(input("Enter x = "))
y = int(input("Enter y = "))
print ((x+y)**2)


