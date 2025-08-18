scores = [19.5, 18, 20, 17, 16.75, 8.75, 2.5]

print(len(scores))

i = 0
s = 0
while i<len(scores):
    s = s+scores[i]
    i = i+1

average = s/len(scores)

# average = (scores[0]+scores[1]+scores[2]+scores[3]+scores[4]+scores[5]+scores[6])/len(scores)

# average = str(average)
print("Average of the scores: " + str(average))

i = 0
while i < 7:
    if scores[i] >= 10:
        print(str(scores[i]) + " passed")
    else:
        print(str(scores[i]) + " failed") 
    i = i+1

# if scores[0] >= 10:
#     print(str(scores[0]) + " passed")
# else:
#     print(str(scores[0]) + " failed")

# if scores[1] >= 10:
#     print(str(scores[1]) + " passed")
# else:
#     print(str(scores[1]) + " failed")

# if scores[2] >= 10:
#     print(str(scores[2]) + " passed")
# else:
#     print(str(scores[2]) + " failed")

# if scores[3] >= 10:
#     print(str(scores[3]) + " passed")
# else:
#     print(str(scores[3]) + " failed")

# if scores[4] >= 10:
#     print(str(scores[4]) + " passed")
# else:
#     print(str(scores[4]) + " failed")

# if scores[5] >= 10:
#     print(str(scores[5]) + " passed")
# else:
#     print(str(scores[5]) + " failed")

# if scores[6] >= 10:
#     print(str(scores[6]) + " passed")
# else:
#     print(str(scores[6]) + " failed")


#exercise 01
names = ["Morteza", "AmirALi", "Mohammad"]

i = 0
while i<len(names):
    print(names[i])
    i = i+1

print("end")



