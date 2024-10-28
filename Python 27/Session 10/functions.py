import numpy as np

def average(numbersList):
    Sum = 0
    for number in numbersList:
        Sum += number
    return Sum/len(numbersList)

def minimum(numbersList):
    Min = np.Inf
    for number in numbersList:
        if number<Min:
            Min = number
    return Min

def maximum(numbersList):
    Max = -1*np.Inf
    for number in numbersList:
        if number>Max:
            Max = number
    return Max

def Variance(numbersList):
    avg = average(numbersList)
    Sum = 0
    for number in numbersList:
        Sum = Sum + (number-avg)**2
    return Sum/len(numbersList)

def StandardDevation(numbersList):
    var = Variance(numbersList)
    return var**(1/2)

def primeNumbers(numbersList):
    primeList = []
    for number in numbersList:
        error = False
        if number <= 2:
            primeList.append(False)
        else:            
            for i in range(2, int(number)):
                if number%i == 0:
                    error = True
            if not error:
                primeList.append(number)
    return primeList
            
    
    
    
    
        
        