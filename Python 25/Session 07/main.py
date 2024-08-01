# # Example

# x = int(input('enter your number: '))

# binary = ''

# while True:
#     r = x%2
#     x = x//2  
#     binary = binary+str(r)
#     if (x == 0):
#         break
    
# print(binary)
# binary = "".join(reversed(binary))
# print('0b'+binary)

students = ['AmirReza', 'Mahdiyar', 'Setayesh', 'Kimiya', 'Nazanin', 'Matin']

print(students)
# print([students[1], students[2]])

# print(students[1:4])

# print(students[2:6])
# print(students[2:])

# print(students[0:3])
# print(students[:3])

# print(students[:])

# print(students[5])
# print(students[-1])

try:
    i = students.index('Kimiya')
    print(i)
    students.pop(i)
    print(students)
except:
    print('your input is not in the list')




# print(type(students))

# print(students[2])

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])
# print(students[5])

# for i in students:
#     print(i)
    
# print(len(students))

# students.append('Morteza')
# print(students)

# students.insert(1, 'Morteza')
# print(students)

# scores = []
# print(scores)

# while True:
#     x = input('enter your score: ')
#     if x == 'q':
#         break
#     else:
#         x = float(x)
#     scores.append(x)
#     print(scores)
    

# print(scores)
# print(len(scores))