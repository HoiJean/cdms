# import os
# import sqlite3
#
# # DEFAULT_PATH = os.path.join(os.path.dirname(__file__), '../database.sqlite3')
# DEFAULT_PATH = os.path.join(os.path.dirname(__file__), '../temp/database.db')
#
#
# class Database:
# 	def __init__(self):
# 		"""Initialize the database connection."""
# 		self.connection = sqlite3.connect(DEFAULT_PATH)
# 		self.cursor = self.connection.cursor()
#
# 	def __del__(self):
# 		self.close()
#
# 	def close(self):
# 		"""Close the connection."""
# 		self.cursor.close()
#
# 	def execute(self, sql):
# 		"""Execute an insert query."""
# 		self.cursor.execute(sql)
#
# 	def fetch_all(self, sql, params=None):
# 		"""Perform fetch all statement, will return an array."""
# 		if params:
# 			self.cursor.execute(sql, (params,))
# 		else:
# 			self.cursor.execute(sql)
#
# 		return self.cursor.fetchall()
#
# 	def fetch_all_by_id(self, table, id):
# 		query = f"SELECT * FROM {table} WHERE id = ?"
# 		return self.fetch_all(query, id)
#
# 	def fetch_single(self, table, id):
# 		query = f"SELECT * FROM {table} WHERE id = ? LIMIT 1"
# 		self.cursor.execute(query, (id,))
# 		return self.cursor.fetchone()
