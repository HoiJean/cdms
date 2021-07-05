from helpers.typevalidation import TypeValidation


class Encryption:

    alpha_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    key = 7

    def __init__(self, key=None):
        if key is not None:
            self.key = key

    def encrypt(self, message):
        if TypeValidation.is_digit(str(message)):
            return message
        result = ""

        for letter in message:
            if letter in self.alpha_capital:
                letter_index = (self.alpha_capital.find(letter) + self.key) % len(self.alpha_capital)
                result = result + self.alpha_capital[letter_index]

            elif letter in self.alpha_lower:
                letter_index = (self.alpha_lower.find(letter) + self.key) % len(self.alpha_lower)
                result = result + self.alpha_lower[letter_index]

            else:
                result = result + letter

        return result

    def decrypt(self, message):
        if TypeValidation.is_digit(str(message)):
            return message
        result = ""

        for letter in message:
            if letter in self.alpha_capital:
                letter_index = (self.alpha_capital.find(letter) - self.key) % len(self.alpha_capital)
                result = result + self.alpha_capital[letter_index]

            elif letter in self.alpha_lower:
                letter_index = (self.alpha_lower.find(letter) - self.key) % len(self.alpha_lower)
                result = result + self.alpha_lower[letter_index]

            else:
                result = result + letter
        return result
