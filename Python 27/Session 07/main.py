# import numpy 

# a = int(input('enter A coeffiecent: '))
# b = int(input('enter B coeffiecent: '))
# c = int(input('enter C coeffiecent: '))

# Coeffs = [a, b, c]

# delta = Coeffs[1]**2 - 4*Coeffs[0]*Coeffs[2]

# if delta < 0:
#     print('There is no Roots for this polynomial!')
# else:
#     x1 = (-Coeffs[1] + numpy.sqrt(delta))/(2*Coeffs[0])
#     x2 = (-Coeffs[1] - numpy.sqrt(delta))/(2*Coeffs[0])
#     print(x1, x2)
    

# a = int(input('enter first side: '))
# b = int(input('enter second side: '))
# c = int(input('enter third side: '))

# sides = [a, b, c, a, b]

# i = 0
# check = False

# while i<3:
#     if sides[i]**2 == (sides[i+1]**2 + sides[i+2]**2):
#         check = not check
#     i = i+1
    
# if check:
#     print('OK')
# else:
#     print('No Triangle')


# a = int(input('enter first side: '))
# b = int(input('enter second side: '))
# c = int(input('enter third side: '))
# sides = [a, b, c]

# for i in sides:
#     print(i)
    
    

Names = ['Morteza', 'Amir', 'Mahla']

i = 0
while i<len(Names):
    print(Names[i])
    i = i+1
    
    
Names = ['Morteza', 'Amir', 'Mahla']

for i in Names:
    print(i)  
    
# myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# myList = range(10)

# newList = [3, 4, 5, 6]
# newList = range(3, 7)

# newList2 = [3, 5, 7, 9]
# newList2 = range(3, 10, 2)


for i in range(10):
    print('Hello')
    
print(0.01 * 100000000)
print(60*60*24)

s = int(input('enter seconds: '))

days = s//86400
r = s%86400
hours = r//3600
r = r%3600
mins = r//60
seconds = r%60


print(f"{days} days | {hours} hours | {mins} minutes | {seconds} seconds ")


