# Lists

name1 = "ShahinJenab"
name2 = "AmirAliGhasemi"
name3 = "NimaAfsarian"
name4 = "NargesJavadi"
name5 = "FatemehJavdani"

print(name1)
print(name2)
print(name3)
print(name4)
print(name5)

names = [name1, "AmirAliGhasemi", name3, name4, "FatemehJavdani"]
i = 0
while i<5:
    print(names[i])
    i = i+1

print(names)
print(names[1])

myInfo = ["Morteza", "Ghoddousi", 31, 1.86, 83, True, ["Volleyball", "Music", "Study"]]
print("First Name: ", myInfo[0])
print("Last Name: ", myInfo[1])
print("Age: ", myInfo[2])
print("Height: ", myInfo[3])
print("Weight: ", myInfo[4])
print("Male: ", myInfo[5])
print("Interests: ", myInfo[6])

print(myInfo[0]+" is interested in "+myInfo[6][0])

# For Loops

print(names)
for i in names:
    print(i)

for i in [0, 2, 4, 6, 8]:
    print(i)

for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in [0, 1, 2]:
    print("hello")

for i in range(3):
    print("hello")
