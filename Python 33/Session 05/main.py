<<<<<<< HEAD
# IF STATEMENT

# if boolean:
#     if's body
#     if's body

# end of the if statement structure

# age = 14

# if age >= 18:
#     print("Access Granted!")
# else:
#     print("Access Denied")



# print("end of the script")


# INPUT FUNCTION

# print("enter your first score:")
n1 = input("enter your first score: ")
n2 = input("enter your second score: ")
n3 = input("enter your third score: ")
n4 = int(input("enter your forth score: "))
n5 = float(input("enter your fifth score: "))

# bool()
# str()

print(type(n1))
print(type(n4))
print(type(n5))

n1 = int(n1)
n2 = int(n2)
n3 = float(n3)


avg = (n1+n2+n3+n4+n5) / 5

if avg >= 10:
    print("passed")
else:
    print("failed")

=======
# while loop 

i = 4

if i<5:
    print(i)

# while condition:
#     while's body

i = 0 # initial point
while i<3: # final condition
    print(i)
    i = i+1 # step

print("end of the script")

i = 0
while i<5:
    print("hello")
    i = i+1

i = 0
while i<10:
    print(i)
    i = i+2

# lists


name1 = "Mohsen"
name2 = "Faramarz"
name3 = 'Morteza'

print(name1)
print(name2)
print(name3)

names = ['Mohsen', "Faramarz", "Morteza"]
print(names)
print(names[0])
print(names[1])
print(names[2])

i = 0
while i<3:
    print(names[i])
    i = i+1

my_info = ["Morteza", 'Ghoddousi', 31, 83, 1.86, True, ["Programming", "VolleyBall", "Music"]]
print(my_info[0])
print(my_info[1])
print(my_info[2])
print(my_info[3])
print(my_info[4])
print(my_info[5])
print(my_info[6])

print(my_info[6][1])

print(my_info)
my_info[3] = 84
print(my_info)

new_list = [my_info[0], my_info[1]]

print(new_list)

new_list1 = my_info[0:2]
print(new_list1)

new_list1 = my_info[:2]
print(new_list1)

new_list2 = my_info[1:5]
print(new_list2)

new_list3 = my_info[4:7]
print(new_list3)

new_list3 = my_info[4:]
print(new_list3)

print(my_info[:])

print(my_info)
my_info.append("gray")
print(my_info)

print(my_info.index(['Programming', 'VolleyBall', 'Music']))

print(my_info)
my_info.pop(6)
print(my_info)

print(my_info)
my_info.insert(2, "Male")
print(my_info)

print(len(my_info))

print(my_info[7])
print(my_info[len(my_info)-1])
print(my_info[-1])

print(my_info[3])
print(my_info[-5])


# # exercise 

# midterm = float(input("enter your midterm score: "))
# final = float(input("enter your final score: "))
# scores = [midterm, final]

# average = (scores[0]+scores[1]) / len(scores)

# print(average)

# exercise 

# score1 = float(input("enter your score: "))
# score2 = float(input("enter your score: "))
# score3 = float(input("enter your score: "))
# score4 = float(input("enter your score: "))
# score5 = float(input("enter your score: "))

# average = (score1 + score2 + score3 + score4 + score5) / 5
# print(average)

scores = []
i = 0
s = 0
while i<3:
    score = float(input("enter your score: "))
    scores.append(score)
    s = s+scores[-1]
    i = i+1

print(scores)

print(s/len(scores))

i = 0
s = 0
while i<3:
    s = s + float(input("enter your score: "))
print(s/3)
>>>>>>> 1a43faee5a04a80bd8e8e96bd37d8ce53618e653
