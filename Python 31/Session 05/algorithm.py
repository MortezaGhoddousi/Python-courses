# x = float(input("enter your score: "))

# if x>=10:
#     print("passed")
# else:
#     print("failed")

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print(x1, x2)
elif delta == 0:    
    x = (-b)/(2*a)
    print(x)
else:
    print("no root")
    
