alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(string: str) -> str:
    """Returns a string with every letter of the original string
       placed three indexes down in the alphabet.
    """
    encoded_string = ''
    for letter in string:
        if letter in alphabet:
            encoded_string += alphabet[alphabet.index(letter) - 3]
        else:
            encoded_string += letter

    return encoded_string


def decode(string: str) -> str:
    """Returns a string with every letter of the original string
       placed three indexes up in the alphabet.
    """
    decoded_string = ''
    for letter in string:
        if letter in alphabet:
            new_index = alphabet.index(letter) + 3
            if new_index > len(alphabet) - 1:
                new_index -= len(alphabet)

            decoded_string += alphabet[new_index]
        else:
            decoded_string += letter

    return decoded_string


encoded = encode('quick brown fox jumps over... the fence?')
print(encoded)
decoded = decode(encoded)
print(decoded)
