import hashlib

def miner(number, prevBlock, data):
    difficulty = 5
    bounce = 0   
    while True:
        dataToHashed = data+str(number)+prevBlock[2]+str(bounce)
        hashedData = hashlib.sha256(dataToHashed.encode()).hexdigest()
        first_five_digits = hashedData[:difficulty]
        if first_five_digits == '0'*difficulty:
            return bounce
        bounce = bounce + 1
    

blocks = []

blocks.append([0, 'sample'+str(0), '000'])

counter = 1
while True:
    data = 'sample'+str(counter)
    number = counter
    b = miner(number, blocks[counter-1], data)
    dataToHashed = data+str(number)+blocks[counter-1][2]+str(b)
    hashedData = hashlib.sha256(dataToHashed.encode()).hexdigest()
    blocks.append([number, data, hashedData])
    print(blocks[counter])
    counter = counter+1
    if counter == 5:
        break
    
print(blocks)



 




