from commands.backupcommand import BackupCommand


class BackupScreen:

	def show(self):
		command = BackupCommand()
		command.execute()

