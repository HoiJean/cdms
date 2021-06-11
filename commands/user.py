from database import database


class User:

    @staticmethod
    def login(username, password):
        db = database.Database()

        cursor = db.cursor
        cursor.execute("SELECT * FROM users WHERE username=? AND password=? LIMIT 1", (username, password))
        result = cursor.fetchone()

        db.connection.commit()

        if result is None:
            return False
        return True
