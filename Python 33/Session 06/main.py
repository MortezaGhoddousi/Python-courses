# ex 1

# x1 = float(input("Enter your first number: "))
# x2 = float(input("Enter your second number: "))
# x3 = float(input("Enter your third number: "))

# if x1 < x2 and x1 < x3:
#     print(x1, "is the lowest number which you have entered")

# if x2 < x1 and x2 < x3:
#     print(x2, "is the lowest number which you have entered")

# if x3 < x2 and x3 < x1:
#     print(x3, "is the lowest number which you have entered")


# admin_user = "admin"
# admin_password = "admin_password"

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == admin_user:
#     if password == admin_password:
#         print("Access Granted")
#     else:
#         print("password is wronge, try again!")
# else:
#     print("Username is wronge")


# # IF ELIF ELSE STATEMENT

# price < $10 => 5%
# 10 < price < 25 => 7.5%
# 25 < price < 70 => 12%
# price > 70 => 30%

# price = float(input("Enter your product price: "))

# if price < 10:
#     discounted_price = price * 0.95
# elif price < 25:
#     discounted_price = price * 0.925
# elif price < 70:
#     discounted_price = price * 0.88
# else:
#     discounted_price = price * 0.7

# print(discounted_price, "$ product price after discounting")

# # # ITERATION STRUCTURE
# # WHILE LOOP

# i = 15 # initial step

# # i < 3 final step (stop criteria)
# while i>3:
#     print(i)
#     i = i-3 # step 


# print("end of the script")


import time

admin_user = "admin"
admin_password = "admin_password"

username = input("Enter your username: ")
password = input("Enter your password: ")

counter = 0

while not (username == admin_user and password == admin_password):
    counter = counter + 1

    print("username or password is wronge, try again")
    if counter == 3:
        print("you have tried so many times, try again after 10 seconds")
        timer = 10
        while timer >= 0:
            print(timer, "left")
            time.sleep(1)
            timer = timer - 1
        counter = 0 
            
    username = input("Enter your username: ")
    password = input("Enter your password: ")

print("Access Granted")
