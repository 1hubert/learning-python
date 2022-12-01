def palindrom(string: str) -> bool:
    string1 = string[:len(string)//2]
    string_backwards = string[::-1]
    string2 = string_backwards[:len(string)//2]

    return string1 == string2


string = 'zamolomaz'
print(palindrom(string))