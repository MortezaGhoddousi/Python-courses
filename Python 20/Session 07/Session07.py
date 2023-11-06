# counter = 5
# while counter>0:
#     student=(input("Enter the name of the student: ")) # the name of student
#     score=(int(input("Enter the score of them: ")))
#     if score >= 10:
#       print(student, "with ","score",score, " is accepted")
#     else:
#        print(student,"with","score",score,"is failed")
#     counter = counter - 1
# print("end of score table")

# Lists

name1 = 'Peyman'; 
name2 = 'Shoeib'; 
name3 = 'Hamid'; 

print(name1, name2, name3)
print(name2)

name = ['Peyman', 
        'Shoeib', 
        'Hamid', 
        19, 
        15.5, 
        True, 
        [10, 15, 14]]

print(name[0])
print(name[2])
print(name[5])
print(name[6][1])

names = ['Peyman', 
        'Shoeib', 
        'Hamid']

# range(3) = [0, 1, 2]
for i in names:
   print(i) 
   
plants = ['apples', 'bannanas', 'pineapples', 'cucumbers', 'peaches', 'onions']
for i in plants:
    print(i)
    
print(plants[1:3])
print(plants[0:4])
print(plants[:4])
print(plants[2:9])
print(plants[2:])
print(plants[:])
print(plants[-1])
print(plants[-3])
print(plants[-3:-1])
print(plants[-3:1])
print(plants[9])