"""
<Description>.

| ``Path``: squadron_ui/api/_resources/_base_resource.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

import typing as tp

if tp.TYPE_CHECKING:
    from .._api_client import ApiClient


class BaseResource:
    """Base shared API resource class."""

    __slots__ = ("_api_client",)

    _api_client: ApiClient

    def __init__(self, api_client: ApiClient) -> None:
        """
        Create an API base resource.

        :param api_client: The parent API client.
        """
        self._api_client = api_client
