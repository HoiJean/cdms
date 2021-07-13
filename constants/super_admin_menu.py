from screens.advisor import Advisor
from screens.backup_screen import BackupScreen
from screens.client import Client
from screens.log_screen import LogScreen
from screens.temp import Temp
from screens.update_login_screen import UpdateLoginScreen

# SUPER ADMIN MENU

super_admin_menu = {
	1: {
		"label": "List of users",
		"func": Advisor().show
	},
	2: {
		"label": "Add advisor",
		"func": Advisor().create
	},
	3: {
		"label": "Modify advisor or admin",
		"func": Advisor().update
	},
	4: {
		"label": "Delete advisor or admin",
		"func": Advisor().delete
	},
	5: {
		"label": "Reset advisor or admin password",
		"func": Advisor().update_password
	},
	6: {
		"label": "Add client",
		"func": Client().create
	},
	7: {
		"label": "Modify client",
		"func": Client().update
	},
	8: {
		"label": "Remove client",
		"func": Client.delete
	},
	9: {
		"label": "Search client",
		"func": Client().show
	},
	10: {
		"label": "Add a new Admin",
		"func": Advisor().create_admin
	},
	11: {
		"label": "Make system backup",
		"func": BackupScreen().show
	},
	12: {
		"label": "System logs",
		"func": LogScreen().show
	},
}
