# Client Data Management System
# Version 0.0
from constants import credentials
from database import database
from screens.login import Login


def print_info(name):
	print("Client Data Management System")


if __name__ == '__main__':
	if credentials.username is None:
		print('You need to login in order to use this app.')
		login = Login()
		login.login_action()

	# database.db_connect()
	# db = database.Database()
	# query = "SELECT * FROM clients"
	# results = db.fetch_all(query)
	#
	# # print(results)
	#
	# single = db.fetch_single("clients", 1)
	# multiple = db.fetch_all_by_id("clients", 1)
	# #
	# print(multiple)
