# from sys import argv

# script = argv

# print ("The script is called:", script)

# def name123_():
    
    
    
# Exercise 1:

def print_evens(a, b):
    for i in range(a, b+1):
        if i%2==0:
            print(f"{i} is even")

print_evens(4, 10)

# Exercise 2:

def revers_str(string):
    maxlen = len(string)
    rev_str = ""
    for l in range(maxlen-1, -1, -1):
        rev_str = rev_str + str(string[l])
    print(rev_str)
        
revers_str("Python18")

# Exercise 3:

def sum_multipy_list_items(mylist):
    sum = 0
    mult = 1
    for item in mylist:
        sum = sum+item
        mult = mult*item
    print(f"sum of items is {sum} and multipy of them is {mult}")

mylist = [4, 6, 2, 3]
sum_multipy_list_items(mylist)

# Exercise 4:

def check_unique(mylist):
    newlist = []
    for item in mylist:
        try:
            if newlist.index(item):
                pass
        except:
            newlist.append(item)
    print(newlist)
  
mylist = [1, 1, 5, 4, 6, 6, 2, 2, 2, 3]  
check_unique(mylist)