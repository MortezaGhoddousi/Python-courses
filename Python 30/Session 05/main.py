# Functions

def f(x, y, z):
    if x<0 and y<0 and z<0:
        return x**2 + 3*x*y*z + ((x**2)*(y**2)) + 3*z
    else:
        return 3*(x**3) + 4*x*(y**2)*z
    
x = f(1, 2, 3)
print(x)
print(f(1, 2, 3))

def f1():
    print('invoking function') 
    print('no input, no output')
    print('end of the function') 

f1()
print('end of the script') 

def f2():
    print('invoking function') 
    print('no input, while have an output')
    y = '1234'
    print('end of the function') 
    return y
    

print(f2())
print('end of the script')

def f3(x, y):
    print('invoking function') 
    print('haveing inputs, while no output')
    z = (x**2 + y**2)**0.5
    print('z:', z)
    print('end of the function') 
    

f3(3, 4)
print('end of the script')

def f4(x, y):
    print('invoking function') 
    print('both inputs and output')
    if x>y:
        print('end of the function') 
        return x
    else:
        print('end of the function') 
        return y 
    
    

print("Maxdimum:", f4(3, 4))
print('end of the script')

# numpy module
import numpy
scores = [4, 5, 15, 17, 19]

print(numpy.amin(scores))
print(numpy.amax(scores))
print(numpy.average(scores))
print(numpy.var(scores))
print(numpy.std(scores))



