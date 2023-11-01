# For loops

for i in range(3):
    print("Hello")
    print(i)

# If statements

temp = 28
if temp > 25:
    print("High temprature")

# While loops

while temp > 25:
    print("High temprature")
    print(temp)
    temp = temp-1
    
print("End")

password = "123"
guess = input("Enter your password: ")
while guess != password:
    print("Your password is wrong!")
    guess = input("Enter your password: ")

print("Login")