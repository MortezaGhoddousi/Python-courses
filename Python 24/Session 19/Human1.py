class Human:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def sayHello(self):
        print(f"Hello {self.fname}!")
        
class Rectangle:
    def __init__(self, width, *args):
        self.width = width
        self.check = False
        if len(args) == 1:
            self.length = args[0]
        else:           
            self.height = args[1]
            self.length = args[0]
            self.check = True
    
    def calArea(self):
        return self.width * self.length
    
    def calPrimeter(self):
        return 2*(self.width * self.length)
    
    def calvolume(self):
        if self.check:
            return self.width * self.height * self.length
        else:
            return self.width * self.length
            