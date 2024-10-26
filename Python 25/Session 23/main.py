my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print (f"If I add {my_age}, {my_height}, and {my_weight} I get {my_age + my_height + my_weight}.")

print ("salam" * 10)





print("There's something going on here.")
print("With the three double-quotes.")
print("We'll be able to type as much as we like.")
print("Even 4 lines if we want, or 5, or 6.")

print(""" 
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.   
      """)


# age = int(input("How old are you? "))

myfile = open('./names.txt')

# content = myfile.read()
# print(content)

names = []

with myfile as f:
    names.append(f.readline())
    
print(names)
 
# میخام فایل names را باز کنم   
with open('names.txt') as f:
    # هر خط داخل فایل را میخانم و در متغیر قرار میدهم
    lines = f.readlines()
    print(lines)
    print(len(lines))

myfile.close()

myfile = open('./names.txt', 'w')


names = ['Matin\n', 'Mahdiar\n']
for i in names:
    myfile.write(i)
    
myfile.close()