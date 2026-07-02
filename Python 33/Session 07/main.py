# Ex1

# Min = 99999999999
# Max = -99999999999

# Sum = 0

# i = 0
# while i<5:
#     number = int(input("enter your number: "))
#     if number < Min:
#         Min = number
#     i = i+1

#     if number > Max:
#         Max = number
    
#     Sum = Sum + number

# print("Minimum of numbers is:", Min)
# print("Maximum of numbers is:", Max)
# print("Average of numbers is:", Sum/5)


# Ex2

# number = int(input("enter your number: "))

# while number >= 0:
#     print(number)
#     number = number - 1

# Ex3

# number = int(input("enter your number: "))

# factorial = 1

# while number > 0:
#     factorial = factorial * number
#     number = number - 1

# print(factorial)

# Ex4

# check = True
# while check:
while True:
    client_name = input("enter your name: ")
    print(client_name.upper())
    print(client_name.lower())
    print(client_name.capitalize())

    if client_name.capitalize() == "Morteza":
        # check = False
        break






