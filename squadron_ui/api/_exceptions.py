"""
<Description>.

| ``Path``: squadron_ui/api/_exceptions.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

import typing as tp


class _SquadronApiError(Exception):
    """
    Generic SquadronApiError class.

    :cvar _DEFAULT_MESSAGE: Default error message displayed in console.
    """

    STATUS_CODE: tp.ClassVar[int] = -1
    _DEFAULT_MESSAGE: tp.ClassVar[str] = "An application error occurred."

    def __init__(
        self,
        message: str | None = None,
        *args: tp.Any,
        **kwargs: tp.Any,
    ) -> None:
        """
        SquadronApiError constructor.

        :param message: Error message.
        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(message or self._DEFAULT_MESSAGE, *args, **kwargs)


class SquadronApiUnhashablePasswordError(_SquadronApiError):
    """Raised when the password is not hashable (Status 400)."""

    STATUS_CODE = 400
    _DEFAULT_MESSAGE = "The given password is not hashable (Status 400)."


class SquadronApiInvalidTokenError(_SquadronApiError):
    """Raised when the API token is invalid (Status 401)."""

    STATUS_CODE = 401
    _DEFAULT_MESSAGE = "Access token is invalid or expired (Status 401)."


class SquadronApiInvalidCredentialsError(_SquadronApiError):
    """Raised when the entered credentials are invalid (Status 401)."""

    STATUS_CODE = 401
    _DEFAULT_MESSAGE = "The given credentials are invalid (Status 401)."


class SquadronApiUserNotFoundError(_SquadronApiError):
    """Raised when the user is not found (Status 404)."""

    STATUS_CODE = 404
    _DEFAULT_MESSAGE = "The user is not found (Status 404)."


class SquadronApiUserAlreadyRegisteredError(_SquadronApiError):
    """Raised when the user is already registered (Status 409)."""

    STATUS_CODE = 409
    _DEFAULT_MESSAGE = "The user is already registered (Status 409)."


class SquadronApiHttpStatusError(_SquadronApiError):
    """Raised when an unknown HTTP status code is returned (Status unknown)."""

    STATUS_CODE = -1
    _DEFAULT_MESSAGE = "An unknown HTTP status code was returned"

    def __init__(
        self,
        status_code: int | str = "Unknown",
        message: str | None = None,
        *args: tp.Any,
        **kwargs: tp.Any,
    ) -> None:
        super().__init__(
            message=(message or self._DEFAULT_MESSAGE) + f"(Status {str(status_code)})",
            *args,
            **kwargs,
        )
