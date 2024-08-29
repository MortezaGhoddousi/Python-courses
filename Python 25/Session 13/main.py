# x = int(input('enter your number: '))
# y = x

# reversedNum = ''

# while True:
#     reversedNum = reversedNum + str(x%10)
#     x = x//10
    
#     if x == 0:
#         break
    
# if int(reversedNum) == y:
#     print('the number is palindrom')
# else: 
#     print('the number is not palindrom')
    
# import matplotlib.pyplot as plt
# import math
# import numpy as np

# # x = range(0, 7, 0.1)
# x = np.linspace(0, 2*math.pi, 50)
# y = []
# for i in x:
#     print(i)
#     y.append(math.sin(i))


# plt.figure()

# plt.plot(x, y)

# plt.show()


import pandas

import matplotlib.pyplot as plt

df = pandas.read_excel('./data.xlsx')

print(len(df))

plt.figure()

plt.stem(range(len(df)), df)

plt.show()