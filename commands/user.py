from database import database
from database import databasemanager


class User:
	def __init__(self):
		self.db_manager = databasemanager.DatabaseManager()

	@staticmethod
	def login_old(username, password):
		db = database.Database()

		cursor = db.cursor
		cursor.execute("SELECT * FROM users WHERE username=? AND password=? LIMIT 1", (username, password))
		result = cursor.fetchone()

		db.connection.commit()

		user_result = {
			"username": result[1],
			"is_admin": result[3],
		}

		if result is None:
			return False
		return user_result

	def login(self, username, password):
		cursor = self.db_manager.select('users', {"username" : username, "password" : password})
		result = cursor.fetchone()

		user_result = {
			"username": result["username"],
			"is_admin": result["is_admin"],
		}

		if result is None:
			return False
		return user_result
