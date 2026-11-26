"""
<Description>.

| ``Path``: squadron_ui/api/_exceptions.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""


class SquadronApiUnhasablePasswordError(Exception):
    """Raised when the password is not hashable (Status 400)."""


class SquadronApiInvalidTokenError(Exception):
    """Raised when the API token is invalid (Status 401)."""


class SquadronApiInvalidCredentialsError(Exception):
    """Raised when the entered credentials are invalid (Status 401)."""


class SquadronApiUserNotFoundError(Exception):
    """Raised when the user is not found (Status 404)."""


class SquadronApiUserAlreadyRegisteredError(Exception):
    """Raised when the user is already registered (Status 409
    )."""
