# Mathematical Operators

x = 7
y = 9.5

z = x + y
print(f"{x} + {y} = {z}")

z = x - y
print(f"{x} - {y} = {z}")

z = x * y
print(f"{x} * {y} = {z}")

z = x / y
print(f"{x} / {y} = {z}")

z = x % y
print(f"{x} % {y} = {z}")

z = x // y
print(f"{x} // {y} = {z}")

z = x ** y
print(f"{x} ** {y} = {z}")

# DATA TYPE CONVERSION
a = '4'
a = int(a)
b = 5

c = a + b

c = float(c)

c = str(c)

firstname = 'morteza'
lastname = 'ghoddousi'

fullname = firstname + lastname
print(fullname)

print(firstname * 3)

# COMPARISON OPERATORS

x = 7
y = 9

z = x < y
print(f"{x} < {y} => {z}")

z = x <= y
print(f"{x} <= {y} => {z}")

z = x > y
print(f"{x} > {y} => {z}")

z = x >= y
print(f"{x} >= {y} => {z}")

z = x == y
print(f"{x} == {y} => {z}")

z = x != y
print(f"{x} != {y} => {z}")

# LOGICAL OPERATORS

print(f"{True} and {True} => {True and True}")
print(f"{True} and {False} => {True and False}")
print(f"{False} and {True} => {False and True}")
print(f"{False} and {False} => {False and False}")

print(f"{True} or {True} => {True or True}")
print(f"{True} or {False} => {True or False}")
print(f"{False} or {True} => {False or True}")
print(f"{False} or {False} => {False or False}")

print(f"not {False} => {not False}")
print(f"not {True} => {not True}")


z = not((True and (4 != 5)) or ((42 > 41.99) or True))
print(z)