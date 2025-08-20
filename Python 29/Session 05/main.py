names = ['Morteza', 'AmirAli', 'Mohammad']

print('Print list cells without loops')
print(names[0])
print(names[1])
print(names[2])

print('Print list cells using while loop')

i = 0
while i<len(names):
    print(names[i])
    i = i+1

print('Print list cells using for loop')

# for variable in list:
#     for's body'

for i in names:
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    print(i)

for i in numbers:
    if i%2 == 0:
        print(i)

numbers1 = [2, 4, 6, 8, 10]
for i in numbers1:
    print(i)



mylist = [0, 1, 2]
mylist2 = range(3)
for m in mylist:
    print('hello')


mylist = ['hello', 'hello', 'hello']
for m in mylist:
    print(m)

mylist3 = range(10) # [0, 1, 2, ..., 10-1]

for i in mylist3:
    print(i+1)
    print('hello')

mylist4 = range(1, 99)

for i in mylist4:
    print(i)


scores = [4, 8, 10, 5.75, 9, 18, 15, 16.5, 20, 17]

s = 0
Max = scores[0]
Min = scores[0]
for i in scores:
    s = s+i
    if i > Max:
        Max = i  
    if i < Min:
        Min = i

average = s/len(scores)
print("Average: " + str(s/len(scores)))
print("Maximum: " + str(Max))
print("Minimum: " + str(Min))

s = 0
for i in scores:
    s = s+(i-average)**2

variance = s/len(scores)
print("variance: " + str(variance))

import numpy
scores = [4, 8, 10, 5.75, 9, 18, 15, 16.5, 20, 17]
Max1 = numpy.amax(scores)
Min1 = numpy.amin(scores)
average1 = numpy.average(scores)
variance1 = numpy.var(scores)

print("Average: " + str(average1))
print("Maximum: " + str(Max1))
print("Minimum: " + str(Min1))
print("variance: " + str(variance1))




