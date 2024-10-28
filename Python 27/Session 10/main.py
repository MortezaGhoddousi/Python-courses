# import functions
# import numpy

# numbers = input('enter your numbers separeted by space: ').split(' ')

# # numbers = numbers.split(' ')

# # i = 0
# # while i<len(numbers):    
# #     numbers[i] = float(numbers[i])   
# #     i = i+1
    
# # for i, n in enumerate(numbers):
# #     numbers[i] = float(n)  
    
# # new = []
# # for n in numbers:
# #     new.append(float(n))
    
# numbers = [float(n) for n in numbers]    

    

# avg = functions.average(numbers)
# Min = functions.minimum(numbers)
# Max = functions.maximum(numbers)
# var = functions.Variance(numbers)
# sd = functions.StandardDevation(numbers)
# pn = functions.primeNumbers(numbers)

# avgNP = numpy.average(numbers)
# MinNP = numpy.amin(numbers)
# MaxNP = numpy.amax(numbers)
# varNP = numpy.var(numbers)
# sdNP = numpy.std(numbers)


# print(avg)
# print(Min)
# print(Max)
# print(var)
# print(sd)
# print(pn)

# print('*'*50)

# print(avgNP)
# print(MinNP)
# print(MaxNP)
# print(varNP)
# print(sdNP)


fname = 'Morteza'
lname = 'Ghoddousi'
age = 30
myInfo = [fname, lname, age]

print(myInfo) 

myInfo[0] = 'Amir'
print(myInfo) 

print(fname, lname)

temp = fname
fname = lname
lname = temp

print(fname, lname)

[fname, lname] = [lname, fname]

print(fname, lname)
