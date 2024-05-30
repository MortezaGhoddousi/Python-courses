# numbers = {0, 1, 2, 3, 4, 5}


# print(3 in numbers)

# nums = {1, 2, 1, 3, 1, 4, 5, 6}
# print(nums)
# nums.add(-7)
# nums.remove(3)
# print(nums)

# print(numbers | nums)
# print(numbers & nums)
# print(numbers - nums)
# print(numbers ^ nums)

# cubes = [i**3 for i in range(5)]
# print(cubes)


# cubes = []

# for i in range(5):
#     cubes.append(i**3)

# print(cubes)

# evens = []

# for i in range(10):
#     if i**2 % 2 == 0:
#         evens.append(i**2)
        
# print(evens)
        
# evens = [i**2 for i in range(10) if i**2 % 2 == 0]

# print(evens)


# vowels = {'a', 'i', 'o', 'u', 'e'}

# myString = input('Enter your word: ')

# output = [i for i in myString if i not in vowels]

# print(output)

def polyNomial(x):
    return x**2 + 5*x + 4

print(polyNomial(-4))

print((lambda x: x**2 + 5*x + 4)(-4))
