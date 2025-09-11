scores = []
Sum = 0
for i in range(10):
    # s = input('enter your score: ')
    # s = float(s)
    # scores.append(s)
    scores.append(float(input('enter your score: ')))
    if scores[-1] >= 10:
        print(f"{scores[-1]} passed")
    else:
        print(f"{scores[-1]} failed")

    Sum = Sum + scores[-1]

average = Sum / len(scores)
print(average)

if average >= 10:
    print(f"{average} passed")
else:
    print(f"{average} failed")



