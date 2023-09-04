# ## String Functions

# name = "morteza"
# lastName = "ghoddousi"

# print(name.upper())
# print(name.lower())
# print(name.capitalize())

# print(name.find("e"))
# print(lastName.find("z"))

## Lists Functions

# mylist = ["Morteza", "Elina", "Ali", "Mohammad", "Iman"]

# print(mylist)
# print(len(mylist))

# for i in range(len(mylist)):
#     # print(mylist[i])
#     if mylist[i] == "Ali":
#         print(i)

# i = 0
# for name in mylist:
#     # print(name)
#     if name == "Ali":
#         print (i)
#     i = i+1

# for index, name in enumerate(mylist):
#     # print(index)
#     # print(name)
#     if name == "Ali":
#         print(index)


# print(mylist)
# mylist.append("Zahra")
# print(mylist)

# mylist.insert(3, "Mobina")
# print(mylist)

# mylist.pop(4)
# print(mylist)

# ind = 0
# for index, name in enumerate(mylist):
#     # print(index)
#     # print(name)
#     if name == "Elina":
#         print(index)
#         ind = index

# ind = mylist.index("Elina")
# print(ind)


## Exersice 1
mylist = []
num_stu = int(input("Enter the number of your students: "))

for i in range(num_stu):
    mylist.append(input(f"Enter your {i+1} name: "))


ind = mylist.index("Elina")
print(f"Index of Elina is in {ind}")
