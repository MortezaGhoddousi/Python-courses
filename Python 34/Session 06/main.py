# MORE ON LISTS

names = ["Alireza", "Mahdiyar", "AmirHossein", "Mohsen", "Abolfazl", "Iliya", "Soheil", "Javad"]

l = len(names)
print(l)

print(names)
names.append("Morteza")
print(names)

names.insert(2, "Iman")
print(names)


try:
    mahdiyars_index = names.index("Mahdiyar")
    print(mahdiyars_index)
    names.pop(names.index("Mahdiyar"))
    print(names)
except ValueError as e:
    print(f"Error: {e}")

print(names[7])
print(names[-2])

new_names = [names[1], names[2], names[3], names[4]]
print(new_names)

new_names1 = names[1:5]
print(new_names1)

new_names2 = names[:3]
print(new_names2)

new_names3 = names[6:]
print(new_names3)

new_names4 = names[:]
print(new_names4)


# FOR LOOPS

# for variable in list:
#     for's body

# length = [0, 1, 2, 3, 4, 5, 6]
length = range(0, 7)

for i in range(7):
    print("hello world")
    print(i)

for n in names:
    print(n)