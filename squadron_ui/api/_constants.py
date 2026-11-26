"""
<Description>.

| ``Path``: squadron_ui/api/_constants.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

from enum import StrEnum


class ApiMethods(StrEnum):
    """Enum of all allowed API methods."""

    GET = "GET"
    POST = "POST"


class ApiGetPaths(StrEnum):
    """Enum of all API GET paths."""

    USER = "/user"
    USER_ME = "/user/me"
    USER_ALL = "/user/all"

    STATUS = "/status"
    STATUS_ME = "/status/me"
    STATUS_ALL = "/status/all"

    ALERTS = "/alerts"


class ApiPostPaths(StrEnum):
    """Enum of all API POST paths."""

    LOGIN = "/login"
    REGISTER = "/register"

    STATUS = "/status"
    ALERT = "/alert"


class ApiSsePaths(StrEnum):
    """Enum of all API SSE paths."""

    EVENTS = "/events"
