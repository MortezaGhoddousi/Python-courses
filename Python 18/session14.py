# # More on Lists

# my_list = [1, 2, 3, 4, 5]
# print(my_list) 

# my_list1 = [num for num in range(1, 6)]
# print(my_list1)

# my_list2 = [num/3 for num in range(1, 6) if num%2==0]
# print(my_list2)


# # Example 1

# num = int(input("Enter your number: "))

# for i in range(num, -1, -1):
#     print(i)

# # Example 2

plaintxt = input("Enter your word: ")

plaintxt = plaintxt.lower()

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 
         "r", "s", "t", "u", "v", "w", "x", "y", "z"]

k = 3
encryptedtxt = ""
for letter in plaintxt:
    ind = chars.index(letter)
    
    encryptedtxt = encryptedtxt+(chars[ind+k])

print(encryptedtxt)

