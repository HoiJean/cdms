import os
import zipfile
import time

from database.databasemanager import DatabaseManager


class BackupCommand:

	def execute(self):
		print("Backup creation is process, please wait...")
		db_manager = DatabaseManager()
		con = db_manager.connection
		data = '\n'.join(con.iterdump())
		filename = f'backup-{time.time()}.zip'

		zf = zipfile.ZipFile(filename, mode='w', compression=zipfile.ZIP_DEFLATED)
		zf.writestr('dump.sql', data)

		if os.path.isfile('log.csv'):
			zf.write('log.csv')

		zf.close()
		print("Backup has been created")
