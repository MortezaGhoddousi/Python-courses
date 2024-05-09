def rect (height, width):
    area = height * width
    primeter = 2 * (height+width)
    return area, primeter

def factorial1(x):
    Sum = 1
    for i in range(x):
        Sum = Sum * (i+1)   
    return Sum

def factorial2(x):
    if x == 1:
        return 1
    else:      
        return x * factorial2(x-1)

