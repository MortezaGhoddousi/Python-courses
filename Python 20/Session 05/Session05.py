# num1 = int(input("first score: "))
# num2 = int(input("second score: "))
# num3 = int(input("third score: "))
# num4 = int(input("forth score: "))
# num5 = int(input("fifth score: "))

# if num1 >= 10:
#     print("Student 1 with score of "+str(num1)+" has passed the course!")
# else:
#     print("Student 1 with score of "+str(num1)+" has failed the course!")
  
# if num2 >= 10:
#     print("Student 2 with score of "+str(num2)+" has passed the course!")
# else:
#     print("Student 2 with score of "+str(num2)+" has failed the course!")
    
# if num3 >= 10:
#     print("Student 3 with score of "+str(num3)+" has passed the course!")
# else:
#     print("Student 3 with score of "+str(num3)+" has failed the course!")
    
# if num4 >= 10:
#     print("Student 4 with score of "+str(num4)+" has passed the course!")
# else:
#     print("Student 4 with score of "+str(num4)+" has failed the course!")
    
# if num5 >= 10:
#     print("Student 5 with score of "+str(num5)+" has passed the course!")
# else:
#     print("Student 5 with score of "+str(num5)+" has failed the course!")  

# print("End")

# num1 = int(input("Enter your score: "))

# # if num1 >= 10:
# #     print("Passed")
# # else:
# #     print("Failed")

# if num1 < 0:
#     print("Invalid")
# elif num1 > 20:
#     print("Invalid")
# elif num1 >= 10 and num1 <= 20:
#     print("Passed")
# else:
#     print("Failed")

num = 5
if num > 10:
    print("Yes")
  
print("lights off")  
presence = False

if presence:
    print("lights on")
    
age = 15
student = False

if age < 18:
    if student:
        print("20%")
    else:
        print("10%")
else:
    print("regular price")
    
if age < 18 and student:
    print("20%")
elif age < 18 and not student:
    print("10%")
else:
    print("regular price")