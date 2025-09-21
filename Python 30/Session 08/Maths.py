class Mathematical:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pi = 3.141592653589793

    def area(self):
        return self.x*self.y
    
    def primeter(self):
        return 2*(self.x+self.y)