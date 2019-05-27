class CaesarCypher:
    def __init__(self, word):
        self.word = word
    def encrypt(self, key):
        new_word = ''
        for char in self.word:
            ascii_char = ord(char)
            if ascii_char > 96 and ascii_char < 123:
                if ascii_char + key > 122:
                    ascii_char = (ascii_char + key) %123 + 97
                else:
                    ascii_char += key
            elif ascii_char > 64 and ascii_char < 91:
                if ascii_char + key > 90:
                    ascii_char = (ascii_char + key) %91 + 65
                else:
                    ascii_char += key
            else:
                raise Exception('Fuck off')
            char = chr(ascii_char)
            new_word += char
        self.word = new_word
    def decrypt(self, key):
        new_word = ''
        for char in self.word:
            ascii_char = ord(char)
            if ascii_char > 96 and ascii_char < 123:
                if ascii_char - key <= 97:
                    ascii_char = 123 - (97 - ascii_char + key)
                else:
                    ascii_char -= key
            elif ascii_char > 64 and ascii_char < 91:
                if ascii_char - key <= 65:
                    ascii_char = 91 - (65 - ascii_char + key)
                else:
                    ascii_char -= key
            else:
                raise Exception('Piss off')
            char = chr(ascii_char)
            new_word += char
        self.word = new_word
example = CaesarCypher('WWW')
example.encrypt(3)
print(example.word)
example.decrypt(3)
print(example.word)