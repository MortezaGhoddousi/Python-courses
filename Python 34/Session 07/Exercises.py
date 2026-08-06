numbers = []

Min = 20
Max = 0
Sum = 0

for n in range(3):
    x = float(input("enter your number: "))
    numbers.append(x)

    Sum = Sum + x

    if x < Min:
        Min = x
    if x > Max:
        Max = x

print(f"Minimum is {Min}")
print(f"Maximum is {Max}")
print(f"Average is {Sum / len(numbers)}")


