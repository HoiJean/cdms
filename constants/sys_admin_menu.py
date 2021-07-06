from screens.backup_screen import BackupScreen
from screens.client import Client
from screens.log_screen import LogScreen
from screens.temp import Temp
from screens.update_login_screen import UpdateLoginScreen

sys_admin_menu = {
    1: {
        "label": "Modify password",
        "func": UpdateLoginScreen().show
    },
    2: {
        "label": "List of users",
        "func": Temp().not_implemented
    },
    3: {
        "label": "Add advisor",
        "func": Temp().not_implemented
    },
    4: {
        "label": "Modify advisor",
        "func": Temp().not_implemented
    },
    5: {
        "label": "Delete advisor",
        "func": Temp().not_implemented
    },
    6: {
        "label": "Reset advisor password",
        "func": Temp().not_implemented
    },
    7: {
        "label": "Make system backup",
        "func": BackupScreen().show
    },
    7: {
        "label": "System logs",
        "func": LogScreen().show
    },
    8: {
        "label": "Add client",
        "func": Client().create
    },
    9: {
        "label": "Modify client",
        "func": Client().update
    },
    10: {
        "label": "Remove client",
        "func": Temp().not_implemented
    },
    11: {
        "label": "Search client",
        "func": Client().show
    },
}