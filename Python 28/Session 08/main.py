# numbers = []
# while True:
#     x = input("Enter the number: ")
#     if x == "q":
#         break   
#     numbers.append(float(x))

# print(numbers)


students = ["Narges", "Fatemeh", "Setayesh", "Nima", "AmirAli", "Shahin"]
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])
print(students[5])

print(students)


newStudents = [students[2], students[3]]
print(newStudents)
newStudents1 = students[2:5]
print(newStudents1)

print(students[5])
ind = students.index("Shahin")
print(ind)
print(students[ind])

print(students[len(students)-1])

print(students[-1])
print(students[-2])
print(students[-3])
print(students[-4])
print(students[-5])
print(students[-6])

print(students)
students.append("Morteza")
print(students)

students.insert(3, "Morteza")
print(students)

students.pop(2)
print(students)

students.pop(students.index("Fatemeh"))
print(students)

students.append("Sahar")
print(students)

import numpy as np
import random
x = [3, 5, 2, 9]

print(random.choice(x))

print(np.amin([3, 5, 2, 9]))
print(np.amax([3, 5, 2, 9]))
print(np.average([3, 5, 2, 9]))
print(np.var([3, 5, 2, 9]))

options = ["rock", "paper", "scissors"]

print(random.choice(options))