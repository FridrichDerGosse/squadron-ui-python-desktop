"""
<Description>.

| ``Path``: squadron_ui/models/_user_status.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 22.11.2026
| ``Authors``: LukasKrah
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class UserStatusData:
    """
    Represents a selected user status.
    """

    number: int
    name: str


class UserStatus(Enum):
    """
    Available user status.
    """

    value: UserStatusData

    READY = UserStatusData(2, "Ready")
    COMING = UserStatusData(3, "Coming")
    ONLINE = UserStatusData(4, "Online")
    OFFLINE = UserStatusData(5, "Offline")
    LEAVING = UserStatusData(6, "Leaving")
