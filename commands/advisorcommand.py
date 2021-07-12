from database import databasemanager

class Advisorcommand:
	def __init__(self):
		self.db_manager = databasemanager.DatabaseManager()

	def create(self, **kwargs):
		self.db_manager.add('users', kwargs)

	def remove(self, **kwargs):
		self.db_manager.delete('users', kwargs)

	def get(self, **kwargs):
		return self.db_manager.select('users', kwargs)

	def search(self, search):
		return self.db_manager._execute("SELECT * FROM clients WHERE full_name LIKE ?", ('%' + search + '%',))

	def update(self, criteria, data):
		self.db_manager.update('users', criteria, data)
