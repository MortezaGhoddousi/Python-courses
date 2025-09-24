# For loops

# for variable in list:
#     body for

# names = ['Morteza', 'Maedeh', 'Shafi']

# print(len(names))

# for name in names:
#     print(name)

# print('end of the script')


# range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# scores = []
# for _ in range(10):
#     score = float(input('enter your score: '))
#     scores.append(score)

# print(scores)

# scores1 = [float(input('enter your score: ')) for _ in range(10)]

# print(scores1)


# While loops

# types of booleans:

# 1- True / False
# 2- Comparison Operators
# 3- Logical Operators

# while condition(boolean):
#     while bod

# scores2 = []

# i = 0
# while i<10:
#     score = float(input('enter your score: '))
#     scores2.append(score)
#     i = i+1

# print(scores2)


# Functions

# def name(arguments):
#     function's body
#     return output

# def getScores(scores):
#     score = float(input('enter your score: '))
#     scores.append(score)
#     return scores

# scores3 = []
# for _ in range(10):
#     scores3 = getScores(scores3)

# print(scores3)

# def sayHello():
#     print("this line is executed by function's body")
#     print("hello world!")

# print("this line is executed by script")
# sayHello()

# Types of variables
# 1- Strings
# 2- Integers
# 3- Floats
# 4- Booleans
# 5- Lists
# 6- Tuples
# 7- Dictionaries
# 8- Sets
# 9- DataFrame -> pandas
# 10- Array -> numpy
# 11- NaN -> numpy
# 12- None


my_none = None
my_string = 'Morteza'
my_integer = 31
my_float = 1.86
my_boolean = True
# lists
my_list = ['Morteza', 'Maedeh', 'Shafi']
print(my_list)
my_list.append('Iman')
print(my_list)

print(my_list.index('Shafi'))

my_list.pop(2)
print(my_list)

my_list[1] = 'Mahmoudi'
print(my_list)


# tuples
my_tuple = ('Morteza', 'Maedeh', 'Shafi', 'Morteza', 'Morteza')
print(my_tuple)
print(my_tuple[0])

print(len(my_tuple))

# my_tuple[1] = 'Mahmoudi'
# my_tuple.append('Iman')

print(my_tuple.index('Shafi'))
print(my_tuple.count('Morteza'))

# dictionaries

info = [
    'Morteza',
    'Ghoddousi',
    31, 
    1.86, 
    83, 
    True
    ]

print(info[0])

my_dict = {
    "firstName": 'Morteza',
    "lastName": 'Ghoddousi',
    "age": 31, 
    "height": 1.86, 
    "weight": 83, 
    "isMale": True
}

print(my_dict['firstName'])
print(my_dict.get('firstName'))

print(my_dict.keys())
print(my_dict.values())

for n in my_dict.values():
    print(n)

print(my_dict)
my_dict.pop('isMale')

print(my_dict)
my_dict.clear()
print(my_dict)


# sets

my_set = {
    'Morteza',
    'Ghoddousi',
    31, 
    1.86, 
    83, 
    'Morteza',
    True
}

print(my_set)

my_set.add('Programming')
print(my_set)



