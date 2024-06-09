def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]

result = list(map(add_five, nums))
print(result)

result1 = []
for i in nums:
    result1.append(add_five(i))
  
print(result1)
  
  
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

res1 = []

for i in nums:
    if i%2==0:
        res1.append(i)

print(res1)

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
        
print(list(numbers(11)))

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
  
print(list(countdown()))    
  
for i1 in countdown(): #[5, 4, 3, 2, 1]
    print(i1)
    
# def infinite_sevens():
#     while True:
#         yield 7
        
# for i in infinite_sevens():
#     print(i)

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")
    
decorated = decor(print_text)
decorated()

def decore(func, x):
    def wrap():
        print("***")
        func(x)
        print("***")
        print("END OF PAGE")
    return wrap
        
               
def print_text(x):
    print(f"INVOICE #{x}")
  
x = input("enter x: ")
myfunction = decore(print_text, x)  
myfunction()


def mydecor(func):
    def changed():
        a = 3.14*2*2
        return func()+a
    return changed


def calPrimeter():
    return 2*3.14*2

calPrimeter = mydecor(calPrimeter)
print(calPrimeter())

print(calPrimeter())
