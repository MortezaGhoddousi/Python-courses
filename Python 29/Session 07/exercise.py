def average(a, b, c):
    Sum = a+b+c
    return Sum/3

def Max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    
def Min(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
    
print(average(5, 8, 2))
print(Max(5, 8, 2))
print(Min(5, 8, 2))

def averageList(numbers):
    Sum = 0
    for n in numbers:
        Sum = Sum + n

    return Sum/len(numbers)

def MinList(numbers):
    m = numbers[0]
    for n in numbers:
        if n < m:
            m = n
    return m

def MaxList(numbers):
    m = numbers[0]
    for n in numbers:
        if n > m:
            m = n
    return m

print(averageList([3, 8, 5, 4, 6]))
print(MinList([3, 8, 5, 4, 6]))
print(MaxList([3, 8, 5, 4, 6]))
