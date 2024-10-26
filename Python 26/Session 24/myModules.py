class Sentences:
    def __init__(self):
        pass
    
    def splitSen(self, sen):
        return sen.split(' ')
    
    def sortedList(self, usList): 
        usList.sort()
        return usList
    
    def deleteFirst(self, sList):
        w = sList.pop(0)
        print(w)
        
    def deleteLast(self, sList):
        w = sList.pop(-1)
        print(w)