import functions

alpha = 0.1

pApple = [1, 0]
tApple = 1

pCucumber = [0, 1]
tCucumber = -1

w = [0, 0]

b = 0


# n = w*p + b

for i in range(10):
    

    n = w[0]*pApple[0] + w[1]*pApple[1] + b

    a = functions.hardlim(n)

    e = tApple - a

    w[0] = w[0] + alpha*(e)*pApple[0]
    w[1] = w[1] + alpha*(e)*pApple[1]

    b = b + alpha*e



    n = w[0]*pCucumber[0] + w[1]*pCucumber[1] + b

    a = functions.hardlim(n)

    e = tCucumber - a

    w[0] = w[0] + alpha*(e)*pCucumber[0]
    w[1] = w[1] + alpha*(e)*pCucumber[1]

    b = b + alpha*e


ptest = [0.2, 0.85]

n = w[0]*ptest[0] + w[1]*ptest[1] + b

a = functions.hardlim(n)

if a == 1:
    print('Apple')
else:
    print('Cucumber')




