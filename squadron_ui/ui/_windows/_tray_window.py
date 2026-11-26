"""
<Description>.

| ``Path``: squadron_ui/ui/_windows/_tray_window.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 22.11.2026
| ``Authors``: LukasKrah
"""

from customtkinter import CTk
import typing as tp

if tp.TYPE_CHECKING:
    from tkinter import Event, Misc


class TrayWindow(CTk):
    """
    Small TopLevel TrayWindow with the core functionality of the program.
    """

    __slots__ = ("__on_focus_out_callback",)

    __on_focus_out_callback: tp.Callable[[Event[Misc]], None] | None

    def __init__(
        self,
        *,
        title: str = "Squadron",
        on_focus_out_callback: tp.Callable[[Event[Misc]], None] | None = None,
    ) -> None:
        super().__init__()

        self.__on_focus_out_callback = on_focus_out_callback

        self.title(title)
        self.lift()
        self.focus_force()

        self.bind("<FocusOut>", self.__on_focus_out)

    def __on_focus_out(self, event: Event[Misc]) -> None:
        self.destroy()
        if self.__on_focus_out_callback is not None:
            self.__on_focus_out_callback(event)
