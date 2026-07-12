def calAvgList(n):
    Sum = 0
    for i in n:
        Sum = Sum + i

    return Sum/len(n)

def calMax(n):
    Max = n[0]
    for i in n:
        if i > Max:
            Max = i
    return Max

def calMin(n):
    Min = n[0]
    for i in n:
        if i < Min:
            Min = i
    return Min

def calVar(n):
    avg = calAvgList(n)
    Sum = 0
    for i in n:
        Sum = Sum + (i-avg)**2

    return Sum/len(n)


Pi_number = 3.14