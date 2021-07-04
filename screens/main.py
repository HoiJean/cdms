from constants import credentials
from helpers.consoleoutput import ConsoleOutput
from helpers.typevalidation import TypeValidation
from screens.client import Client


class Main:

	@staticmethod
	def index_action():
		action_list = [
			{'name': 'Open client'},
			{'name': 'Register new client'},
			{'name': 'Update client'},
			# {'name': 'Update user password', 'class': Client.index()},
		]

		if credentials.role == 1:
			action_list += [
				{'name': "Add advisor"},
				{'name': "Update advisor"}
			]

		user_input = ''
		while user_input != 'q':

			print(f'Item Choices:')
			for index, item in enumerate(action_list):
				print(f'{index}: {item["name"]}')

			user_input = input('press number to select an option...')

			if not TypeValidation.is_digit(user_input):
				ConsoleOutput.error('Please use a number')
			elif int(user_input) > (len(action_list) - 1):
				ConsoleOutput.error('Please select in range of the options...')
			else:
				# Code is found, todo: check if authorized to perform this action

				if not action_list[int(user_input)]:
					print('Can\'t find this action')
				else:
					if int(user_input) == 0:
						client_obj = Client()
						client_obj.show()
					elif int(user_input) == 1:
						client_obj = Client()
						client_obj.create()
					elif int(user_input) == 2:
						client_obj = Client()
						client_obj.update()
