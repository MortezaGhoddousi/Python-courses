<<<<<<< HEAD
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






=======
# for variable in list:
#     for's body


names = ["Morteza", "Mohsen", "Faramarz"]

i = 0
while i<len(names):
    print(names[i])
    i = i+1

for i in names:
    print(i)

i = 0
while i<3:
    print("hello world")
    i = i+1

# [0, 1, 2]
for i in range(3):
    print("Hello world")

name = "morteza ghoddousi"

for n in name:
    print(n)

print(name[:3])

print(name.upper())
print(name.lower())
print(name.capitalize())

# i = 0
# s = 0
# Max = 0
# Min = 20

# scores = []

# while i<3:
#     score = float(input("Enter your score: "))
#     scores.append(score)
#     s = s+score

#     if score>Max:
#         Max = score

#     if score<Min:
#         Min = score

#     i = i+1

# average = s/3
# print(Min, Max)
# print(s/3)

# i = 0
# s = 0
# while i<3:
#     s = s+(scores[i]-average)**2
#     i =i+1

# variance = s/3
# std = variance**0.5
# print(variance)
# print(std)

# import numpy

# avg = numpy.average(scores)
# Max = numpy.amax(scores)
# Min = numpy.amin(scores)
# var = numpy.var(scores)
# std = numpy.std(scores)

# print(avg, Max, Min, var, std)


word = input("enter your word: ").lower()
# word = word.lower()
counter = 0

vowels = ['a', 'e', 'i', 'o', 'u']

for l in word:
    # if l=="a" or l=='e' or l=='i' or l=='o' or l=="u":
    #     counter = counter+1

    if l in vowels:
        counter = counter+1

print(counter)
>>>>>>> 1a43faee5a04a80bd8e8e96bd37d8ce53618e653
