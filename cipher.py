import string

full_characters = (
    " "
    + string.ascii_letters
    + string.digits
    + string.punctuation
)

#full_characters = " " + string.printable
n = len(full_characters)
positions = {char: index for index, char in enumerate(full_characters)}
#numbers = range(0,n)
#positions = {char:num for char,num in zip(full_characters,numbers)}

def encoder(any_message, key):
    """This program encrypts any message you give it with a key"""
    encoded_message = ""
    for letter in any_message:
        get_position = positions[letter]
        shift = (get_position + key)%n
        get_letter = full_characters[shift]
        encoded_message += get_letter
    return encoded_message


def decoder(encoded_message, key):
    """This program decrypts any message you give it with a key"""
    decoded_message = ""
    for letter in encoded_message:
        get_position = positions[letter]
        shift = (get_position - key)%n
        get_letter = full_characters[shift]
        decoded_message += get_letter
    return decoded_message