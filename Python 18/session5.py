# x = range(3)

# for y in x:
#     print(y)

# x = ["Morteza", "Elina"]

# for y in x:
#     print(y)

# for i in range(10):
#     print("hello")

# seats = 20

# while seats > 0:
#     print("Ticket sold")
#     seats = seats-1

# print("The end")


password = "123"
guess = input("Enter your password: ")
while guess != password:
    print("Password is incorrect")
    guess = input("Enter your password: ")

print("Password Granted!")