from screens.client import Client
from screens.temp import Temp
from screens.update_login_screen import UpdateLoginScreen

advisor_menu = {
    1: {
        "label": "Modify password",
        "func": UpdateLoginScreen().show
    },
    2: {
        "label": "Add client",
        "func": Client().create
    },
    3: {
        "label": "Modify client",
        "func": Client().update
    },
    4: {
        "label": "Search client",
        "func": Client().show
    },
}