class BOOK:
    def __init__(self, title, author, yearPublished, isHardcover = True):
        self.title = title
        self.author = author
        self.yearPublished = yearPublished
        self.isHardcover = isHardcover
    
    def getSummary(self):
        result = 'title: '+ self.title + '\n author: ' + self.author + '\n yearPublished: ' + str(self.yearPublished) + '\n isHardcover: ' + str(self.isHardcover)
        return result

    def setIsHardcover(self, isHardcover):
        self.isHardcover = isHardcover
        

class Archive(BOOK):
    def __init__(self):
        self.archive = []
    
    def defNewBook(self, title, author, yearPublished, isHardcover = True):
        super().__init__(title, author, yearPublished, isHardcover = True)
               
    def addBook(self, book):
        self.archive.append(book)
        
    def showBooks(self):
        for b in self.archive:
            print(b)
            

arch = Archive()

arch.defNewBook('Biganeh', 'Alber Kamo', 1945 , False)
arch.addBook(arch.getSummary())

arch.defNewBook('JenayadMokafat', 'Dastayofski', 1800 , False)
arch.addBook(arch.getSummary())

arch.defNewBook('LittlePrince', 'Morteza', 2010 , True)
arch.addBook(arch.getSummary())

arch.showBooks()
