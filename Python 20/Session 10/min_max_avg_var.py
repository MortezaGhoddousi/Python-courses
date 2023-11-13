import math

def calmin_max(numbers):
    min = math.inf
    max = -math.inf
    sum = 0
    for number in numbers:
        sum = sum+number
        if (number>max):
            max = number
        if (number<min):
            min = number
    return max, min

def calavg_var(numbers):
    sum = 0
    for number in numbers:
        sum = sum+number
    avg = sum/len(numbers)
    sum = 0
    for number in numbers:
        sum = sum+((number-avg)**2)
    var = sum/5
    return avg, var
        
