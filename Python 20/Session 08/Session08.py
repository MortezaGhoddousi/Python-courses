# people = [["Morteza", "Peyman", "Shoeib", "Danial"], 
#           ["Ghoddousi", "Nazari", "Rezania", "Hamidi"],
#           [29, 41, 37, 27]]

# print(people[0][2])
# print(people[1][2])
# print(people[2][2])

def f (x):
    print(2*x+3)
  
  
x = 3
f(x)
f(10)
f(9)
f(4)

def sayhello (x):
    print("Hello" + x)
    print("The end of function")

print("end")

sayhello("Morteza")


def sum_two (x, y):
    z = x+y
    return z

a = sum_two(4, 9)
print(a) 

a = sum_two(2, 5)
print(a)

name = "Morteza"

print(name.lower())
print(name.upper())

print(name.find("o"))

lastname = 'ghoddousi'

print(lastname.find("d"))


people = [["Morteza", "Peyman", "Shoeib", "Danial"], 
          ["Ghoddousi", "Nazari", "Rezania", "Hamidi"],
          [29, 41, 37, 27]]

print(len(people))

people.append(["male", "male", "male", "male",])
print(len(people))
print(people)

people.append(14)
print(len(people))
print(people)

people.insert(2, True)
print(people)

people.pop(5)
print(people)

def BMI(w,h):
    index = w/(h*h)
    print(index)
    
BMI(86, 185)
BMI(97, 183)


