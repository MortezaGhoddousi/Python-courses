# sentence = input('enter your sentece: ').split(' ')

# newHash = ''
# for word in sentence:
#     newHash = newHash + word[0]
    
# print(newHash)

import hashlib

# fname = 'Morteza'

# hashedName = hashlib.sha256(fname.encode('utf-8')).hexdigest()

# print(type(hashedName))


for i in range(10000000):
    hashedName = hashlib.sha256(str(i).encode('utf-8')).hexdigest()
    if hashedName[0:8] == '0000000':
        print(i)
        x = i
        break
    
hashedName = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
print(hashedName)