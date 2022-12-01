#test = 'a' > 'A' #(True)
#print(test)

def alphabetSoup(string):
    li = sorted(list(string))
    newString = ''
    for char in li:
        newString += char

    return newString

# word = 'hello'
# print(alphabetSoup(word))

def alphabetSoupB(string):
    li = sorted(list(string))
    lowerLi = sorted(list(string.lower()))
    caps = []
    newString = ''
    
    for char in li:
        if char.isupper():
            caps.append(char)

    for letter in lowerLi:
        if caps.count(letter.upper()) != 0:
            newString += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else:
            newString += letter

    return newString







word = input('Please enter a string: ')
print(alphabetSoupB(word))

