def calAvg_Min_Max_Var(x):
    Sum = 0
    Max = x[0]
    Min = x[0]

    for n in x:
        Sum = Sum + n
        if n > Max:
            Max = n

        if n < Min:
            Min = n

    Avg = Sum / len(x)

    Sum = 0
    for n in x:
        Sum = Sum + (n-Avg)**2
    Var = Sum / len(x)


    return Avg, Min, Max, Var

x = [3, 5, 2, 9]
y = calAvg_Min_Max_Var(x)
print("Avg:", y[0])
print("Min:", y[1])
print("Max:", y[2])
print("Var:", y[3])