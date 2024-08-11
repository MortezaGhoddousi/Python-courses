name = "Morteza,AmirReza,Mahdiyar,Setayesh,Kimia,Nazanin"

myNames1 = name.split(',')
print(myNames1)

word = ''

myNames = []

for l in name:
    if l == ",":
        myNames.append(word)
        print(word)
        word = ''
    else:
        word = word+l

print(word)
myNames.append(word)
    
print(myNames)