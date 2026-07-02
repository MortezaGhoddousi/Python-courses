<<<<<<< HEAD
# comparison operators

x = 4
y = 7

print("4 < 7 =", x < y)
print("4 <= 7 =", x <= y)
print("4 > 7  =", x > y)
print("4 >= 7 =", x >= y)
print("4 == 7 =", x == y)
print("4 != 7 =", x != y)

# logical operators

print("True and True =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False =", False and False)

print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)

print("not False =", not False)
print("not True =", not True)

# Exercise 

x1 = 4
x2 = 8
x3 = 6
x4 = 11
x5 = 2

avg = (x1 + x2 + x3 + x4 + x5) / 5
var = ((x1-avg)**2 + (x2-avg)**2 + (x3-avg)**2 + (x4-avg)**2 + (x5-avg)**2) / 5

print(var)
=======
# comparison operators
x = 5
y = 8

z = x<y
print(str(x)+"<"+str(y)+"=>"+str(z))

z = x<=y
print(str(x)+"<="+str(y)+"=>"+str(z))

z = x>y
print(str(x)+">"+str(y)+"=>"+str(z))

z = x>=y
print(str(x)+">="+str(y)+"=>"+str(z))

z = x==y
print(str(x)+"=="+str(y)+"=>"+str(z))

z = x!=y
print(str(x)+"!="+str(y)+"=>"+str(z))

# logical operators

x = True
y = True
z = x and y
print(str(x)+" and "+str(y)+" => "+str(z))

x = True
y = False
z = x and y
print(str(x)+" and "+str(y)+" => "+str(z))

x = False
y = True
z = x and y
print(str(x)+" and "+str(y)+" => "+str(z))

x = False
y = False
z = x and y
print(str(x)+" and "+str(y)+" => "+str(z))

x = True
y = True
z = x or y
print(str(x)+" or "+str(y)+" => "+str(z))

x = True
y = False
z = x or y
print(str(x)+" or "+str(y)+" => "+str(z))

x = False
y = True
z = x or y
print(str(x)+" or "+str(y)+" => "+str(z))

x = False
y = False
z = x or y
print(str(x)+" or "+str(y)+" => "+str(z))


x = True
z = not x
print("not "+str(x)+" => "+str(z))

x = False
z = not x
print("not "+str(x)+" => "+str(z))



a = True and False
print(a)

light_on = True
door_locked = False
print(light_on or door_locked)
print(light_on and door_locked)


# if statement

age = 22

if age>=18:
    print("you are an adult person")
    print("if's body")
    print("end of the if body")
else:
    print("you are a child")
    print("else's body")
    print("end of the else body")


print("end of the script")

score = float(input("enter your score: "))

if score >= 10 and score <= 20:
    print("passed")
elif score >= 0 and score < 10:
    print("failed")
else:
    print("score is invalid")

is_male = input("enter your gender(male or female): ")

if is_male == "male":
    print("Male")
else:
    print("Female")

>>>>>>> 1a43faee5a04a80bd8e8e96bd37d8ce53618e653
