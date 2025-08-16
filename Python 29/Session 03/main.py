# # Exercise 1
# num1 = float(input("Enter your first number: ")) 
# num2 = float(input("Enter your second number: ")) 
# num3 = float(input("Enter your third number: "))

# average = (num1 + num2 + num3) / 3
# print(f"The average of numbers: {average}")

# if num1 > num2 and num1 > num3:
#     print(f"Maximum of numbers: {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"Maximum of numbers: {num2}")
# else:
#     print(f"Maximum of numbers: {num3}")

# if num1 < num2 and num1 < num3:
#     print(f"Minimum of numbers: {num1}")
# elif num2 < num1 and num2 < num3:
#     print(f"Minimum of numbers: {num2}")
# else:
#     print(f"Minimum of numbers: {num3}")

# print(num2)
# # variables: list

# numbers = [num1, num2, num3, "average", average, True]
# print(numbers)
# print(numbers[1])

Information = [
                ["Morteza", "Ghoddousi", True, 1.86, 83], 
                ["AmirAli", "Shafi", True, 1.73, 50]
            ]

print(Information[0][1])
print(Information[1][0], Information[1][1])

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
gender = input("sex(male/female): ")
if gender == 'male':
    gender = True
else:
    gender = False
height = float(input('Enter your height: '))
weight = int(input('Enter your weight: '))

print(Information)
# Information.append([firstName, lastName, gender, height, weight])
Information.insert(1, [firstName, lastName, gender, height, weight])
print(Information)

