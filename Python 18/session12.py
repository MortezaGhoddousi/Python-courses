def SplittingWords(arg):
    words = arg.split(' ')
    return words

def FirstWord(arg):
    return arg.split(' ')[0]

def LastWord(arg):
    return arg.split(' ')[-1]

string = "Hello world!";

print(SplittingWords(string))
print(FirstWord(string))
print(LastWord(string))