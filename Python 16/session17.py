# # Defination Decimal to Binary and Binary to Decimal Functions

# def dec_bin(x):
#     arr = []
#     check = True
#     while check:
#         arr.append(x%2)
#         x = x//2
#         if x < 2:
#             arr.append(x)
#             arr.reverse()
#             return arr

# def bin_dec(x):
#     sum = 0
#     x.reverse()
#     for i in range(len(x)-1, -1, -1):
#         sum = sum+((2**i)*x[i])
#     return sum

# num = int(input("Enter the number: "))  
# y = dec_bin(num)
# print(y)

# z = bin_dec(y)
# print(z)

# # Rock Paper Scissor

# import random

# # x=1 => Rock
# # x=2 => Paper
# # x=3 => Scissor
# AI = random.randint(1, 3)

# Player = int(input("Enter your choose: (an Integer number in range of 1 to 3)"))

# if (AI==Player):
#     print(AI)
#     print(Player)
#     print("Draw")
# if (AI==1) and (Player==2):
#     print(AI)
#     print(Player)
#     print("Player won")
# if (AI==1) and (Player==3):
#     print(AI)
#     print(Player)
#     print("AI won")
# if (AI==2) and (Player==1):
#     print(AI)
#     print(Player)
#     print("AI won")
# if (AI==2) and (Player==3):
#     print(AI)
#     print(Player)
#     print("Player won")
# if (AI==3) and (Player==1):
#     print(AI)
#     print(Player)
#     print("Player won")
# if (AI==3) and (Player==2):
#     print(AI)
#     print(Player)
#     print("AI won")


# # WCI

# temp = int (input ("Enter the air temprature: "))
# windspeed = int (input ("Enter the wind speed: "))
# wci = 13.12+(0.6215*temp)-(11.37*(windspeed**0.16))+(0.3965*temp*(windspeed**0.16))
# print(f"WCI is {wci}")

# # Seller Problem

# check = True
# sell = []
# profit = []
# sum = 0
# while check:
#     item = float(input("Enter your sold stuff: "))
#     if item==0:
#         check = False
#         tax = (sum*9)/100
#         Profit = sum-tax
#     else:
#         sell.append(item)
#         profit.append((item*10)/12)
#         sum = sum+profit[-1]
#     print(sell)
#     print(profit)

# print(f"Total price is {sum}")
# print(f"Your Profit is {Profit}")


# # Printing stars

# n = int(input("Enter number of lines: "))

# for i in range(n):
#     print(i*"*")

# Checking the number of digits in an integer number

def check_digit(x):
    i = 1
    check = True
    while check:
        if x//10!=0:
            i = i+1
            x = x//10
        else:
            return i


x = int(input("Enter your number: "))

y = check_digit(x)

if y == 8:
    print(x)
else:
    t = abs(8-y)
    print(x*(10**t))

