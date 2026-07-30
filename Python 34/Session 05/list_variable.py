# LISTS

name1 = "Alireza"
name2 = "Mahdiyar"
name3 = "AmirHossein"
name4 = "Mohsen"
name5 = "Abolfazl"
name6 = "Iliya"
name7 = "Soheil"
name8 = "Javad"

print(name1)
print(name2)
print(name3)
print(name4)
print(name5)
print(name6)
print(name7)
print(name8)


names = ["Alireza", "Mahdiyar", "AmirHossein", "Mohsen", "Abolfazl", "Iliya", "Soheil", "Javad"]
ages = [17, 17, 17, 17, 17, 17, 17, 18]

print(type(names))

print(names)

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print(names[7])

print("While loop")

i = 0
while i < 8:
    print(f"{names[i]} - {ages[i]}")
    i = i+1

myInfo = ["Morteza", "Ghoddousi", 32, 80, 1.86, True]