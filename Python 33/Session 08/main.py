name1 = "Bahareh"
name2 = "Mahdieh"
name3 = "Pooria"
name4 = "Abolfazl"
name5 = "Mahtab"
name6 = "Maryam"

print(name1)
print(name2)
print(name3)
print(name4)
print(name5)
print(name6)

name6 = "Iman"

names = ["Bahareh", "Mahdieh", "Pooria", "Abolfazl", "Mahtab", "Maryam"]

print(names[0])
print(names[1])
print(names[2])


myInfo = ["Morteza", "Ghoddousi", 32, 1.86, True, ["Programming", "Reading", "Watching Movie"]]

print(myInfo[0])

print(myInfo[4])

myInfo[2] = 33
print(myInfo[2])

print(myInfo)

print(myInfo[5][1])


myInfo2 = [myInfo[1], myInfo[2], myInfo[3], myInfo[4]]

print(myInfo2)

myInfo3 = myInfo[1:5]
print(myInfo3)

print(myInfo[0:3])
print(myInfo[:3])

print(myInfo[4:6])
print(myInfo[4:])

print(myInfo[:])

print(myInfo[5])
print(myInfo[-1])

print(myInfo[2])
print(myInfo[-4])

print(len(myInfo))

print(myInfo.index(33))

print(myInfo)
myInfo.pop(myInfo.index(33))
print(myInfo)

myInfo.append(32)
print(myInfo)

myInfo.insert(4, 32)
print(myInfo)

myInfo.reverse()
print(myInfo)
