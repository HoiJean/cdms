from database import databasemanager

class Clientcommand:
	def __init__(self):
		self.db_manager = databasemanager.DatabaseManager()

	def create(self, **kwargs):
		self.db_manager.add('clients', kwargs)

	def remove(self, **kwargs):
		self.db_manager.delete('clients', kwargs)

	def get(self, **kwargs):
		return self.db_manager.select('clients', kwargs)

	def search(self, search):
		return self.db_manager._execute("SELECT * FROM clients WHERE full_name LIKE ?", ('%' + search + '%',))

	def update(self, criteria, data):
		self.db_manager.update('clients', criteria, data)
