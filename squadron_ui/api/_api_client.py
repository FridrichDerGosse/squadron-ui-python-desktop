"""
<Description>.

| ``Path``: squadron_ui/api/_api_client.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

lazy from httpx import URL, Client, Response

lazy from ._constants import ApiGetPaths, ApiMethods, ApiPostPaths
lazy from ._resources import AuthResource


class ApiClient:
    """
    Core HTTP client for the API. Manages the session, auth token and base errors.
    """

    __slots__ = ("__client", "__auth")

    __client: Client

    __auth: AuthResource

    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self.__client = Client(
            base_url=base_url,
            timeout=timeout,
            headers={"Content-Type": "application/json"},
        )

    def set_token(self, token: str) -> None:
        """
        Attach a bearer token to all following requests.

        :param token: Token value
        """
        self.__client.headers["Authorization"] = f"Bearer {token}"

    def clear_token(self) -> None:
        """Remove the configured bearer token."""
        self.__client.headers.pop("Authorization", None)

    def request(self, method: ApiMethods, path: ApiGetPaths | ApiPostPaths) -> Response:
        """
        Send http request to the API.

        :param method: Used HTTP method
        :param path: Path to send the request to
        :return: Response
        """
        return self.__client.request(
            method=method.value,
            url=path,
        )

    def get(self, path: ApiGetPaths) -> Response: ...

    def post(self, path: ApiPostPaths) -> Response: ...
