# ## Example1
# # range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(10):
#     for j in range(10):
#         print(str(i)+"*"+str(j)+"="+str(i*j))

# ## Example2

# cel = float(input("Enter temperature: "))
# farh = (cel*1.8)+32
# print(cel, farh)

# ## Example3

# import numpy
# word = input("enter your word: ").lower()

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# i = numpy.zeros([len(alphabet)], dtype=int)

# print(len(alphabet))
# print(len(i))

# for l in word:
#     index = alphabet.index(l)
#     i[index] = i[index]+1

# c = 0
# for l in alphabet:
#     print("counter of "+str(l)+" = "+str(i[c]))
#     c = c+1

# Example4

# number = int(input("Enter your number: "))
# r = number%2
# if r == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")