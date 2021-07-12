from constants import credentials
from database import database
from database import databasemanager
import hashlib


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
		password = self.hash_password(password)
		cursor = self.db_manager.select('users', {"username": username, "password": password})
		result = cursor.fetchone()

		if result is None:
			return False

		user_result = {
			"username": result["username"],
			"is_admin": result["is_admin"],
		}

		credentials.current_user = result
		return user_result

	def update_password(self, new_password, user=None):
		current_user = credentials.current_user
		if user is not None:
			current_user = user

		new_password = self.hash_password(new_password)
		criteria = {"id": current_user["id"]}
		data = {"password": new_password}
		cursor = self.db_manager.update('users', criteria, data)

	@staticmethod
	def hash_password(text):
		text = str(text).encode('utf-8')
		return hashlib.md5(text).hexdigest()
