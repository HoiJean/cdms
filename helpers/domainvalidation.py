import re


class DomainValidation:

	@staticmethod
	def validate(validation_type, message_name, error_output, min_length=3, max_length=100):
		validated = False
		user_input = ""
		while not validated:
			user_input = input(message_name)

			if not re.match(validation_type, user_input, re.IGNORECASE):
				print(error_output)
			else:
				if len(user_input) < min_length:
					print(f"Input too low, must be minimum {min_length} characters")
				elif len(user_input) > max_length:
					print(f"Input too big, must be minimum {max_length} characters")
				else:
					validated = True
		return user_input

	@staticmethod
	def validateOptionalFields(validation_type, message_name, error_output, min_length=3, max_length=100):
		validated = False
		user_input = input(message_name)

		if len(user_input) < 1:
			return False

		while not validated:

			if not re.match(validation_type, user_input, re.IGNORECASE):
				print(error_output)
			else:
				if len(user_input) < min_length:
					print("Too short")
				elif len(user_input) > max_length:
					print("Too long")
				else:
					validated = True
		return user_input

	@staticmethod
	def accept_all(message_name):
		user_input = input(message_name)
		return user_input
