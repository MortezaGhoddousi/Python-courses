def calAverage(x):
    Sum = 0
    for s in x:
        Sum = Sum+s
    return Sum / len(x)

scores = [4, 5, 15, 17, 19]
print(f'average: {calAverage(scores)}')

def checkPass(x):
    if x >= 10:
        print(f'{x} passed')
    else:
        print(f'{x} failed')

def calVariance(x):
    Sum = 0
    avg = calAverage(x)
    for s in x:
        Sum = Sum + (s-avg)**2
    return Sum / len(x)

def calMin(x):
    Min = x[0]
    for s in x:
        if s<Min:
            Min = s
    return Min

def calMax(x):
    Max = x[0]
    for s in x:
        if s>Max:
            Max = s
    return Max

print(f'variance: {calVariance(scores)}')
print(f'minimum: {calMin(scores)}')
print(f'maximum: {calMax(scores)}')
     
checkPass(calAverage(scores))

for score in scores:
    checkPass(score)
