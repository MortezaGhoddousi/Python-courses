letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
plaintext = input("Enter your message: ")

K = 24

# Encryption
encryptedtext = []
for letter in plaintext:
    i = letters.index(letter)
    i = i+K
    if i>=len(letters):
        i = i-len(letters)
    encryptedtext.append(letters[i])

print(encryptedtext)   
    
#Decryption
decryptedtext = []
for letter in encryptedtext:
    i = letters.index(letter)
    i = i-K
    if i<0:
        i = i+len(letters)
    decryptedtext.append(letters[i])

print(decryptedtext)

# Breaking the encrypted text
for K in range(len(letters)):
    decryptedtext = []
    for letter in encryptedtext:
        i = letters.index(letter)
        i = i-K
        if i<0:
            i = i+len(letters)
        decryptedtext.append(letters[i])
    print(decryptedtext)


    
