# Lists
myList = ["Morteza", "Narges", "Fatemeh", "AmirAli", "Shahin"]
print(myList)
print(type(myList))

myList.pop(2)
i = 0
while i<len(myList):
    print(myList[i])
    i = i+1


myList[2] = "Negar"
print(myList)

# Tuples
myTuple = ("Morteza", "Narges", "Fatemeh", "AmirAli", "Shahin", "Fatemeh")
print(myTuple)
print(type(myTuple))

try:
    myTuple[2] = "Negar"
    print(myTuple)
except:
    print("Assigning to a tuple is not supported!")

print(myTuple.count("Fatemeh"))
print(myTuple.index("Fatemeh"))

# Sets
mySet = {"Morteza", "Narges", "Fatemeh", "AmirAli", "Shahin", "Fatemeh"}
print(mySet)
print(type(mySet))


try:
    mySet[2] = "Negar"
    print(mySet)
except:
    print("Assigning to a set is not supported!")

mySet.add("Negar")
print(mySet)

for x in mySet:
  print(x)

print("Fatemeh" in mySet)

# Dictionaries

myDict = {
    "students": ["Narges", "Fatemeh", "AmirAli", "Shahin"],
    "teacher": ["Morteza"],
    "class": "Python",
    0: "level"
}

print(myDict["class"])
print(myDict["students"][1])
print(myDict.keys())

try:
    print(myDict["Teacher"])
except:
    print("MortezaGhoddousi")

print(myDict.get("Teacher", "MortezaGhoddousi"))

print(myDict.items())
myDict.pop("class")
print(myDict)

myDict["students"].pop(1)
print(myDict)
