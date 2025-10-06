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

