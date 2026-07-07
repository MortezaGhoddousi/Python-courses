# TUPLES

myList = ["Morteza", "Ghoddousi", 32, 1.86, 82, True]

myTuple = ("Morteza", "Ghoddousi", 32, 1.86, 82, True)

print(myList[1])
print(myTuple[1])

print(myList)
myList[2] = 33
print(myList)

# myTuple[2] = 33

myList.append("Male")
print(myList)

print(myTuple.index("Morteza"))

# DICTIONARIES

myDict = {
    "first_name": "Morteza", 
    "last_name": "Ghoddousi", 
    "age": 32, 
    "height": 1.86, 
    "weight": 82, 
    "is_male": True
}

print(myDict["last_name"])
print(myDict.get("last_name"))

# print(myDict["Height"])
print(myDict.get("heeight", 1.5))

print(myDict.keys())
print(myDict.values())

print(myDict)
myDict.popitem()
print(myDict)

myDict.pop("age")
print(myDict)

myDict["age"] = 33
print(myDict)

myDict["age"] = 32
print(myDict)


# SETS
mySet = {"Morteza", "Ghoddousi", 32, 1.86, 82, True, 32}
print(mySet)

mySet.add(35)
print(mySet)

try:
    mySet.remove(32)
    mySet.remove("morteza")
except:
    print("there is an issue on removing value from the set")
finally:
    print("end of the try except finally structure")


print(mySet)


print("end")



