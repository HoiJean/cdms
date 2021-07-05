from helpers.typevalidation import TypeValidation


class Encryption:

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = 18732490247

    def __init__(self, key=None):
        if key is not None:
            self.key = key

    def encrypt(self, message):
        if TypeValidation.is_digit(str(message)):
            return message
        message = message.upper()
        result = ""

        for letter in message:
            if letter in self.alpha:
                letter_index = (self.alpha.find(letter) + self.key) % len(self.alpha)

                result = result + self.alpha[letter_index]
            else:
                result = result + letter

        return result

    def decrypt(self, message):
        message = message.upper()
        result = ""

        for letter in message:
            if letter in self.alpha:
                letter_index = (self.alpha.find(letter) - self.key) % len(self.alpha)

                result = result + self.alpha[letter_index]
            else:
                result = result + letter
        return result
