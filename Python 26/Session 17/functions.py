
def encrypted(p, k):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't', 'u' , 'v', 'w', 'x', 'y', 'z']
    encryptedText = ''
    for i in p:
        ind = alphabets.index(i)
        if ind+k > len(alphabets)-1:
            newInd = ind+k-len(alphabets)
        else:
            newInd = ind+k
        encryptedText = encryptedText+alphabets[newInd]
    return encryptedText

def decrypted(c, k):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't', 'u' , 'v', 'w', 'x', 'y', 'z']
    plainText = ''
    for i in c:
        ind = alphabets.index(i)
        if ind-k < 0:
            newInd = ind-k+len(alphabets)
        else:
            newInd = ind-k
        plainText = plainText + alphabets[newInd]
    return plainText

def brootforceAttack(c):
    possibleAnswers = []
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't', 'u' , 'v', 'w', 'x', 'y', 'z']
    for k in range(26):
        plainText = ''
        for i in c:
            ind = alphabets.index(i)
            if ind-k < 0:
                newInd = ind-k+len(alphabets)
            else:
                newInd = ind-k
            plainText = plainText + alphabets[newInd]
        possibleAnswers.append(plainText)
    return possibleAnswers
        