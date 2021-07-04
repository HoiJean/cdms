from database import databasemanager

class Clientcommand:
	def __init__(self):
		self.db_manager = databasemanager.DatabaseManager()

	def create(self, **kwargs):
		self.db_manager.add('clients', kwargs)

	def remove(self, **kwargs):
		pass

	def get(self, **kwargs):
		pass

	def update(self, **kwargs):
		pass
