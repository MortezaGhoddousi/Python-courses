import random

# Generate Uppercase alphabets
UpperChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
         "W", "X", "Y", "Z"]

# Generate Lowercase alphabets
LowerChars = [letter.lower() for letter in UpperChars]

# Generate UNumbers
NumberChars = [i for i in range(10)]

# Putting all of them together
Chars = []
Chars.append(UpperChars)
Chars.append(LowerChars)
Chars.append(NumberChars)
print(Chars)

Charactes_produced = []
for i in range(len(Chars)):
    for j in Chars[i]:
        Charactes_produced.append(j)
print(Charactes_produced)

# Taking length of password from user

Length = int(input("Enter length of your password: "))

# Generating random password 

Password = [random.choice(Charactes_produced) for i in range(Length)]

emptyStringPassword = ""
for i in Password:
    emptyStringPassword = emptyStringPassword+str(i)

print(Password)
print(f"Your password is: {emptyStringPassword}")