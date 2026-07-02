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

# a = float(input("enter a: "))
# b = float(input("enter b: "))

# if a>b:
#     print(a)
# else:
#     print(b)


a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)

    print(x1, x2)
elif delta == 0:
    x = -b/(2*a)
    print(x)
else:
    print("no root")
