"""
Defines a cross-platform pystray wrapper.

Supports left-click, right-click, and debounced hover.

| ``Path``: squadron_ui/tray/_tray_manager.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 22.11.2026
| ``Authors``: LukasKrah
"""

from __future__ import annotations

import typing as tp

if tp.TYPE_CHECKING:
    from PIL import Image


class TrayController:
    """
    Cross-platform pystray wrapper.
    """

    __slots__ = (
        "__name",
        "__title"
    )

    # region InstanceVars
    __name: str
    __title: str
    __icon_image: Image.Image
    __hover_open_delay: float
    __hover_off_debounce: float
    __hover_radius: int
    __on_left_click: ...
    __on_right_click: ...
    __on_hover_enter: ...
    __on_hover_leave: ...

    __hover_state: ...
    __hover_enter_timestamp: ...
    __hover_leave_timestamp: ...
    # endregion
