def rect (x=1, y=1):
    area = x*y
    primeter = 2*(x+y)
    return area, primeter


x = 4
y = 6

area, primeter = rect(x, y)
print("area is " + str(area))
print("primeter is " + str(primeter))

area, primeter = rect(10)
print("area is " + str(area))
print("primeter is " + str(primeter))