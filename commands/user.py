from database import database


class User:

	@staticmethod
	def login(username, password):
		db = database.Database()

		cursor = db.cursor
		cursor.execute("SELECT * FROM users WHERE username=? AND password=? LIMIT 1", (username, password))
		result = cursor.fetchone()

		print("Result type")
		print(result)

		db.connection.commit()

		user_result = {
			"username": result[1],
			"is_admin": result[3],
		}

		if result is None:
			return False
		return user_result
