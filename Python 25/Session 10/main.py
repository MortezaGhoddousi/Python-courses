import numpy
myList = [5, 7, 1, 15, 9, 20, 0, 14, 16] 

# print(numpy.sort(myList))

for i in range(len(myList)):
    for j in range(i+1, len(myList)):
        if myList[i] > myList[j]:          
            myList[j], myList[i] = myList[i], myList[j]
            
print(myList)
            
        

