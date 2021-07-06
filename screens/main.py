from constants import credentials
from constants.advisors_menu import advisor_menu
from constants.sys_admin_menu import sys_admin_menu
from helpers.menuinterface import MenuInterface


class Main:

	@staticmethod
	def index_action():

		menu = advisor_menu

		if credentials.role == 1:
			menu = sys_admin_menu

		# Menu heading and nested dict are sent as arguments
		menu_interface = MenuInterface()
		menu_interface.choose_menu("===MAIN MENU===", menu)