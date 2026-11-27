"""
<Description>.

| ``Path``: squadron_ui/api/_api_client.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

import typing as tp

from httpx import AsyncClient, HTTPStatusError

from api import SquadronApiInvalidTokenError, SquadronApiUserNotFoundError
from ._constants import ApiMethods
from ._resources import AuthResource

from ._exceptions import (
    SquadronApiUnhashablePasswordError,
    SquadronApiUserAlreadyRegisteredError,
    SquadronApiHttpStatusError,
)

if tp.TYPE_CHECKING:
    from httpx import Response
    from ._constants import ApiGetPaths, ApiPostPaths


class ApiClient:
    """
    Core HTTP client for the API. Manages the session, auth token and base errors.
    """

    __slots__ = ("__client", "__auth")

    __client: AsyncClient

    __auth: AuthResource

    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self.__client = AsyncClient(base_url=base_url, timeout=timeout)

        self.__auth = AuthResource(api_client=self)

    def set_token(self, token: str) -> None:
        """
        Attach a bearer token to all following requests.

        :param token: Token value
        """
        self.__client.headers["Authorization"] = f"Bearer {token}"

    def clear_token(self) -> None:
        """Remove the configured bearer token."""
        self.__client.headers.pop("Authorization", None)

    async def request(
        self,
        method: ApiMethods,
        path: ApiGetPaths | ApiPostPaths,
        *,
        data: tp.Mapping[str, tp.Any] | None = None,
    ) -> Response:
        """
        Send http request to the API.

        :param method: Used HTTP method
        :param path: Path to send the request to
        :param data: Data/Parameters to send
        :return: Response
        :raises HTTPStatusError: If one occurred
        """
        response: Response = await self.__client.request(
            method=method.value, url=path.value, data=data
        )
        try:
            response.raise_for_status()
        except HTTPStatusError as error:
            match response.status_code:
                case SquadronApiUnhashablePasswordError.STATUS_CODE:
                    raise SquadronApiUnhashablePasswordError from error

                case SquadronApiInvalidTokenError.STATUS_CODE:
                    raise SquadronApiInvalidTokenError from error

                case SquadronApiUserNotFoundError.STATUS_CODE:
                    raise SquadronApiUserNotFoundError from error

                case SquadronApiUserAlreadyRegisteredError.STATUS_CODE:
                    raise SquadronApiUserAlreadyRegisteredError from error

                case _:
                    raise SquadronApiHttpStatusError(
                        status=response.status_code
                    ) from error

        return response

    async def get(
        self,
        path: ApiGetPaths,
        *,
        data: tp.Mapping[str, tp.Any] | None = None,
    ) -> Response:
        """
        Send http GET request to the API.

        :param path: Path to send the request to
        :param data: Data/Parameters to send
        :return: Response
        :raises HTTPStatusError: If one occurred
        """
        return await self.request(ApiMethods.GET, path, data=data)

    async def post(
        self,
        path: ApiPostPaths,
        *,
        data: tp.Mapping[str, tp.Any] | None = None,
    ) -> Response:
        """
        Send http POST request to the API.

        :param path: Path to send the request to
        :param data: Data/Parameters to send
        :return: Response
        :raises HTTPStatusError: If one occurred
        """
        return await self.request(ApiMethods.POST, path, data=data)

    @property
    def auth(self) -> AuthResource:
        """
        AuthResource for login/register/logout.

        :return: AuthResource
        """
        return self.__auth
