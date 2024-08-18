# # Example 1

# myList = input("Enter your list: ")

# myList = [eval(i) for i in myList.split(',')]

# print(myList)
# myList.sort(reverse=True)
# print(myList)

# # Example 2

# myList = input("Enter your list: ")

# myList = [eval(i) for i in myList.split(',')]

# counter = 0

# for i in myList:
#     counter = counter +1
    
# print("The length of your list is: " + str(counter))
# print("The length of your list is: " + str(len(myList)))

# # Example 3

# import numpy
# myList = input("Enter your list: ")

# myList = [eval(i) for i in myList.split(',')]

# if len(myList)%2 == 0:
#     l = int(len(myList)/2)
#     firstHalf = myList[:l]
#     secondHalf = myList[l:]
# else:
#     l = int(len(myList)/2)
#     firstHalf = myList[:l]
#     secondHalf = myList[l+1:]
  
# newList = [] 
# for i in firstHalf:
#     for j in secondHalf:
#         newList.append(i+j)
        
   
# print(firstHalf) 
# print(secondHalf) 
# print(firstHalf + secondHalf)
# print(newList)

# print(numpy.sum(newList))

b = 4

def f(a):
    print(b)
    if a>5:
        return 2*a+1
    else:
        return 2*a
    
print(f(3))
print(b)
# print(a)
   
x = f(3)
y = f(6)

print(x)
print(y)





