class rect:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def calArea(self):
        return self.width * self.length
    
    def calPrimeter(self):
        return 2 * (self.width + self.length)
    
    def showRes(self, a, p):
        print(f"area of the rect is {a} and primeter of it is {p}")
    
r1 = rect(4, 5)

print(r1.calArea())
print(r1.calPrimeter())

class square(rect):
    def __init__(self, width):
        self.width = width
        
    def calArea(self):
        return self.width**2
    
    def calPrimeter(self):
        return self.width*4
    
    def showRes(self, a, p):
        print(f"area of the rect is {a} and primeter of it is {p} for the square")




r1.showRes(r1.calArea(), r1.calPrimeter())

# print(r1, 'hello', 'third argument')

r2 = square(4)

r2.showRes(r2.calArea(), r2.calPrimeter())


# import numpy as np

# myNum = []
# for i in range(5):
#     myNum.append(int(input('enter the number: ')))
    
# print(np.amax(myNum))

# def calMax(number):
#     Max = -1*np.inf
#     for i in number:
#         if i > Max:
#             Max = i
#     return Max

# print(calMax(myNum))    

# def calMax1(*args):
#     Max = -1*np.inf
#     for i in args:
#         if i > Max:
#             Max = i
#     return Max
        
    

# print(calMax1(4, 5, 10, 14, 8, 10, 29))

# def calMax2(x=0, y=0, *args, **kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(kwargs)
    
    
    
# calMax2(4, 5, 10, 14, 8, 10, 29, z = 14, h = 52)

# def calArea(x=0, y=1):
#     return x * y

# print(calArea())    