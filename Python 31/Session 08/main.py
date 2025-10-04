import numpy as np

print(np.amax([4, 8, 9, 2]))
print(np.amin([4, 8, 9, 2]))
print(np.average([4, 8, 9, 2]))
print(np.var([4, 8, 9, 2]))

from MathClass import mathematical, rect

math1 = mathematical([4, 8, 9, 2])  
math2 = mathematical([14, 8.5, 9, 22])  

print(math1.cal_max())
print(math1.cal_min())
print(math1.cal_avg())
print(math1.cal_var())

print(math2.cal_max())

r1 = rect(2, 4)
r2 = rect(3, 6)

print(r1.area())
print(r2.area())

print(r1.primeter())
print(r2.primeter())


class rect2(rect):

    def __init__(self, w, l):
        self.w = w
        self.l = l

    # def area(self):
    #     return self.w*self.l
    
    def primeter(self):
        return 2*(self.w+self.l)

    def area(self, w, l):
        return w*l

    def volume(self, h):
        return self.w*self.l*h
    
r3 = rect2(5, 2)
print(r3.area(3, 2))
print(r3.primeter())
print(r3.volume(2))

x = 2

x = 3