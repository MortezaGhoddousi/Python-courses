# i = 0

# while i<3:
#     print('hello')
#     i = i+1
    
    
# print('end')



x = 2
myFile = open('./primeNumbers.txt', 'w')


while x < 1000:
    
    y = 0
    i = 2
    
    while i < x:
        if x%i == 0:
            y = 1
        i = i+1
    
    if not y == 1:
        print(f"{x} is prime")
        myFile.write(f"{x} \n")
    x = x+1
    
    