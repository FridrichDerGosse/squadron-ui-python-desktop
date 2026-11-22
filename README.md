# squadron-ui-python-desktop

Brainstorming Ideas:

- Tray Icon (by default should be disableable)
    - Low Resource Usage in Background Mode (delete GUI after x seconds)
    - Left click: Primary UI window
    - Right click: One-View Dashboard
    - Hover: Basic Info?
- Notifications (still in discussion either through SSE, Websockets or Long Polling)
- Views (general not specific to window) (i want to keep the UI very simple):
    - Login (quite obvious) (keep logged in) (server, name, password)
    - Register? (not sure if we do this xD)
    - Main Dashboard (Status selection and overview of others, set notifications)
    - Settings
- Settings
    - Tray Mode
    - Run in background
    - Notifications general
    - Autostart
    - Auto Update / manual update
    - Theme
    - Newsletter on/off...
- Tested support for windows, macos and linux

how (here is important that they support windows, mac and linux)

- Python 3.14
- UI with Customtkinter
- Tray icon with pystray
- notifications idk maybe over ctk or real os notifications
- rest idk yet
