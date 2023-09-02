# age = int(input("Enter your age: "))

# if age >= 18 and age < 50:
#     print("Adult")
# elif age >= 50:
#     print("Elderly")
# else:
#     print("Teenager")


# print("The end")

# age = int(input("Enter your age: "))
# is_student = True
# if age <= 18:
#     if is_student:
#         print("20 percent Discount")
#     else:
#         print("10 percent Discount")
# else:
#     print("Regular Price")


x1 = int(input("Enter the score: "))
x2 = int(input("Enter the score: "))
x3 = int(input("Enter the score: "))

avg = (x1+x2+x3)/3
print(f"Average of scores is: {avg}")

max = -1
min = 21

if x1 > max:
    max = x1
if x2 > max:
    max = x2
if x3 > max:
    max = x3

if x1 < min:
    min = x1
if x2 < min:
    min = x2
if x3 < min:
    min = x3

print(f"Minimum of scores is: {min}")
print(f"Maximum of scores is: {max}")




