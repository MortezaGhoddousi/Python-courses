def findRoots(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return [x1, x2]
    elif delta == 0:
        x = (-b) / (2*a)
        return [x]
    else:
        return False
    
a = float(input("Enter a coefficient for polynomial: "))
b = float(input("Enter b coefficient for polynomial: "))
c = float(input("Enter c coefficient for polynomial: "))

roots = findRoots(a, b, c)

if not roots:
    print("There is no root for this equation.")
else:
    for root in roots:
        print(root)

