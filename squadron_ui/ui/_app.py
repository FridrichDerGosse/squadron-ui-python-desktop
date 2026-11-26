"""
<Description>.

| ``Path``: squadron_ui/ui/_app.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 21.11.2026
| ``Authors``: LukasKrah
"""

import typing as tp

from ._windows import TrayWindow

if tp.TYPE_CHECKING:
    ...


class App:
    """
    Application manager
    """
    __slots__ = (
        "__tray_window",
        "__tray_window_visible"
    )

    __tray_window: TrayWindow | None
    __tray_window_visible: bool

    def __init__(self) -> None:
        self.__tray_window = None
        self.__tray_window_visible = False
    
    def show_tray_window(self) -> None:
        self.__tray_window = TrayWindow()
        self.__tray_window_visible = True

        self.__tray_window.mainloop()


