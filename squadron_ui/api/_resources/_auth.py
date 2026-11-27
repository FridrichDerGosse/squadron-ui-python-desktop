"""
<Description>.

| ``Path``: squadron_ui/api/_resources/_auth.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

import typing as tp
from ._base_resource import BaseResource

from .._constants import ApiPostPaths
from .._models import RegisterResponse, LoginResponse


if tp.TYPE_CHECKING:
    from httpx import Response


class AuthResource(BaseResource):
    """Auth resource."""

    async def login(self, username: str, password: str) -> LoginResponse:
        response: Response = await self._api_client.post(
            ApiPostPaths.LOGIN,
            data={"username": username, "password": password},
        )

        validated_response: LoginResponse = LoginResponse.model_validate(
            response.json()
        )

        return validated_response

    async def register(self, username: str, password: str) -> RegisterResponse:
        response: Response = await self._api_client.post(
            ApiPostPaths.REGISTER,
            data={"username": username, "password": password},
        )

        validated_response: RegisterResponse = RegisterResponse.model_validate(
            response.json()
        )

        return validated_response
