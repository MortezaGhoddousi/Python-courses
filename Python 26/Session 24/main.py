from myModules import Sentences
# import myModules
        
s = Sentences()

sent = "This is an Important sentence!"

usList = s.splitSen(sent)
print(usList)

sList = s.sortedList(usList)
print(sList)

s.deleteFirst(sList)
s.deleteLast(sList)





    
    