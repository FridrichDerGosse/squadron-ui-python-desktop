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

if tp.TYPE_CHECKING:
    from .._models import ApiTokenType


class AuthResource(BaseResource):
    """Auth resource."""

    def login(self, username: str, password: str) -> ApiTokenType:
        self._api_client.post(ApiPostPaths.LOGIN)

        return ""

    def register(self, username: str, password: str) -> None:
        self._api_client.post(ApiPostPaths.LOGIN)

    def logout(self) -> None: ...
