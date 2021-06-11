# Client Data Management System
# Version 0.0

from database import database


def print_info(name):
	print("Client Data Management System")


if __name__ == '__main__':
	# database.db_connect()
	db = database.Database()
	query = "SELECT * FROM clients"
	results = db.fetch_all(query)

	# print(results)

	single = db.fetch_single("clients", 1)
	multiple = db.fetch_all_by_id("clients", 1)
	#
	print(multiple)
