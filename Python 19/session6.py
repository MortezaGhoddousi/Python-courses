

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

plainText = "PYTHONISFUN"

key = 15

## Encryption
EncryptedText = []
encryptedText = ""
for letter in plainText:
    ind = letters.index(letter)
    if ind+key > len(letters)-1:
        ind = ind+key-len(letters)
    else:
        ind = ind+key
    EncryptedText.append(letters[ind])
    encryptedText = encryptedText+letters[ind]

print(encryptedText)


## Decryption
DecryptedText = []
decryptedText = ""
for letter in encryptedText:
    ind = letters.index(letter)
    if ind-key < 0:
            ind = ind-key+len(letters)
    else:
        ind = ind-key
    DecryptedText.append(letters[ind])
    decryptedText = decryptedText+letters[ind]

print(decryptedText)


## Breaking the text
for key in range(len(letters)):
    DecryptedText = []
    decryptedText = ""
    for letter in encryptedText:
        ind = letters.index(letter)
        if ind-key < 0:
                ind = ind-key+len(letters)
        else:
            ind = ind-key
        DecryptedText.append(letters[ind])
        decryptedText = decryptedText+letters[ind]

    print(decryptedText)

