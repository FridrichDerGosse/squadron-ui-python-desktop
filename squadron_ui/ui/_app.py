"""
<Description>.

| ``Path``: squadron_ui/ui/_app.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 21.11.2026
| ``Authors``: LukasKrah
"""

from __future__ import annotations

import typing as tp

from customtkinter import CTk

if tp.TYPE_CHECKING:
    ...


class App(CTk):
    """
    Invisible root application window.
    """

    def __init__(self) -> None:
        super().__init__()
        self.withdraw()
