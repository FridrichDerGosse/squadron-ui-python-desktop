"""
<Description>.

| ``Path``: /main.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 21.11.2026
| ``Authors``: LukasKrah
"""

from squadron_ui.ui import App

import asyncio
import os

with open(".env") as f:
    for line in f:
        if "=" in line and not line.startswith("#"):
            key, val = line.strip().split("=", 1)
            os.environ[key] = val.strip("\"'")


from squadron_ui.api import ApiClient

api_key = os.getenv("SERVER_URl")
api_key = "" if api_key is None else api_key

api = ApiClient(base_url=api_key)


asyncio.run(api.auth.login(username="Test5", password="123"))

exit()
if __name__ == "__main__":
    app_ui = App()

    app_ui.show_tray_window()
