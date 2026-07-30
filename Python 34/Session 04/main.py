# IF STATEMENT

age = 15

if age >= 18:
    print("if's body")
    print("Adult")
    print(age)


print("end of the script")

# IF-ELSE STATEMENT

age = 15

if age >= 18:
    print("if's body")
    print("Adult")
    print(age)
else:
    print("else's body")
    print("Teenager")
    print(age)


print("end of the script")

# IF-ELIF-ELSE STATEMENT

# age = input()
# age = int(age)

age = int(input("Enter your age:"))

if age < 10:
    print("child")
elif age >= 10 and age < 18:
    print("teenager")
elif age >= 18 and age < 50:
    print("adult")
else:
    print("elder")


print("end of the script")




