import time

start = time.time()
i = 0
while i<1000000:
    print(i)
    i = i+1

end = time.time()
whileTime = end-start

start = time.time()
for i in range(1000000):
    print(i)

end = time.time()
forTime = end-start

print(whileTime)
print(forTime)

