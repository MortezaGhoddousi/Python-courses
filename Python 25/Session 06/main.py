
try:  
    num = int(input('enter the number: '))
    while num<2:
        num = int(input('enter the number again: '))
    # for num in range(2, 51):      
    i = 2
    c = 0

    while i < num:
        if num%i==0:
            c = c+1
        i = i+1
        
    if c > 0:
        print(f'{num} is not prime')
    else:
        print(f'{num} is prime')

except:
    print('your input is not correct!')
    