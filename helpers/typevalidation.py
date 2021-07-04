import re


class TypeValidation:

	@staticmethod
	def is_digit(check_input):
		'''
		function checking if your string is a pure digit, int
		return : bool
		'''
		if check_input.isdigit():
			return True
		return False

	@staticmethod
	def is_string_only(check_input):
		'''
		function checking if your string is all letters
		return : bool
		'''
		if check_input.isalpha():
			return True
		return False

	@staticmethod
	def is_string_with_space(check_input):
		'''
		function checking if your string is all letters, but including space(s)
		return : bool
		'''
		valid = False
		if ' ' in check_input:
			for char in check_input:
				if char.isdigit():
					valid = False
				elif char.isalpha() or char.isspace():
					valid = True
		return valid

	@staticmethod
	def is_string_or_num(check_input):
		'''
		function checking if your string is all letters or numbers
		return : bool
		'''
		if check_input.isalnum():
			return True
		return False

	@staticmethod
	def is_float(check_input):
		'''
		function checking if your string is a floating point
		return : bool
		'''
		if '.' in check_input:
			split_number = check_input.split('.')
			if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
				return True
		return False

	@staticmethod
	def is_strong_password(password):
		# calculating the length
		length_error = len(password) < 8

		# searching for digits
		digit_error = re.search(r"\d", password) is None

		# searching for uppercase
		uppercase_error = re.search(r"[A-Z]", password) is None

		# searching for lowercase
		lowercase_error = re.search(r"[a-z]", password) is None

		# searching for symbols
		symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

		# overall result
		password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

		return {
			'password_ok': password_ok,
			'length_error': length_error,
			'digit_error': digit_error,
			'uppercase_error': uppercase_error,
			'lowercase_error': lowercase_error,
			'symbol_error': symbol_error,
		}
