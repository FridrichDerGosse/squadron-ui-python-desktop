"""
<Description>.

| ``Path``: squadron_ui/api/_models.py
| ``Project``: squadron-ui-python-desktop
| ``Created``: 26.11.2026
| ``Authors``: LukasKrah
"""

from pydantic import BaseModel

type ApiTokenType = str


class User(BaseModel):
    id: int
    username: str
    status: int
    info: str


class RegisterResponse(BaseModel):
    success: bool
    user: User


class LoginResponse(BaseModel):
    access_token: ApiTokenType
    token_type: str
