from screens.advisor import Advisor
from screens.backup_screen import BackupScreen
from screens.client import Client
from screens.log_screen import LogScreen
from screens.update_login_screen import UpdateLoginScreen

sys_admin_menu = {
    1: {
        "label": "Modify password",
        "func": UpdateLoginScreen().show
    },
    2: {
        "label": "List of users",
        "func": Advisor().show
    },
    3: {
        "label": "Add advisor",
        "func": Advisor().create
    },
    4: {
        "label": "Modify advisor",
        "func": Advisor().update
    },
    5: {
        "label": "Delete advisor",
        "func": Advisor().delete
    },
    6: {
        "label": "Reset advisor password",
        "func": Advisor().update_password
    },
    7: {
        "label": "Make system backup",
        "func": BackupScreen().show
    },
    8: {
        "label": "System logs",
        "func": LogScreen().show
    },
    9: {
        "label": "Add client",
        "func": Client().create
    },
    10: {
        "label": "Modify client",
        "func": Client().update
    },
    11: {
        "label": "Remove client",
        "func": Client().delete
    },
    12: {
        "label": "Search client",
        "func": Client().show
    },
}
