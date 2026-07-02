# IF STATEMENT

# if boolean:
#     if's body
#     if's body

# end of the if statement structure

# age = 14

# if age >= 18:
#     print("Access Granted!")
# else:
#     print("Access Denied")



# print("end of the script")


# INPUT FUNCTION

# print("enter your first score:")
n1 = input("enter your first score: ")
n2 = input("enter your second score: ")
n3 = input("enter your third score: ")
n4 = int(input("enter your forth score: "))
n5 = float(input("enter your fifth score: "))

# bool()
# str()

print(type(n1))
print(type(n4))
print(type(n5))

n1 = int(n1)
n2 = int(n2)
n3 = float(n3)


avg = (n1+n2+n3+n4+n5) / 5

if avg >= 10:
    print("passed")
else:
    print("failed")

