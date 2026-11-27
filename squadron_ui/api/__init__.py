"""
<Description>.

| ``Path``: squadron_ui/api/__init__.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

from ._exceptions import (
    SquadronApiUserAlreadyRegisteredError,
    SquadronApiUserNotFoundError,
    SquadronApiInvalidTokenError,
    SquadronApiUnhashablePasswordError,
    SquadronApiInvalidCredentialsError,
)

from ._api_client import ApiClient
