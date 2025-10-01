def bmi(w, h):
    i = w/(h*h)
    return i

morteza_bmi_index = bmi(83, 1.86)
print(morteza_bmi_index)

shafi_bmi_index = bmi(48, 1.73)
print(shafi_bmi_index)

maedeh_bmi_index = bmi(62, 1.69)
print(maedeh_bmi_index)

def rectangle(l1, l2):
    area = l1*l2
    primeter = 2*(l1+l2)

    return (area, primeter)

(a1, p1) = rectangle(2, 3)

print(a1)
print(p1)

def rect(d1:float, d2:float) -> tuple:
    area = d1 * d2
    perimeter = 2 * d1 + 2 * d2
    return (area, perimeter)

(x, y) = rect(5, 8)
(x, y) = rect(d2=5, d1=8)

def greeting():
    print("Hello")

greeting()

print(3, 4, 5)

def print2(*a:tuple, **line:dict) -> None:
    print(a)
    print(line)

print2(3, 4, 5, printLine=True, firstName="Morteza")

def print3(a, line):
    print(a)
    print(line)

print3(3, 4)


n = [2, 4, 6, 8]
res = 1

n1 = [n[1], n[2]]

n2 = n[1:3]
print(n)
print(n1)
print(n2)
for x in n2:
    res = res * x
print(res)


cubes1 = []
for i in range(5):
    if i%2 == 0:
        cubes1.append(i**3)

cubes2 = [i**3 for i in range(5) if i%2==0]

print(cubes1)
print(cubes2)

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def add_numbers():
    print("Hello Morteza")

add_numbers()

# myDecor = decor(add_numbers, 2, 4)
# myDecor()




