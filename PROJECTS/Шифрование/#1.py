import string

plain_text = 'Maks'
shift = 5
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift] # Смещение символов

table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)

