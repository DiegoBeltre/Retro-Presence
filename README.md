# Retro Presence

Retro Presence is a Python application that automatically detects the **retro game** currently displayed in OBS Studio and updates your Discord Rich Presence in real time.

Unlike emulator-specific Rich Presence applications, Retro Presence identifies games by analyzing the OBS video feed using perceptual image hashing. Because detection is based entirely on the video stream, it works with both original hardware and emulators.

As long as OBS can see the game, Retro Presence can identify it.

---

## Features

- 🎮 Automatic retro game detection
- 💬 Discord Rich Presence integration
- 📺 OBS Studio integration through WebSocket
- 🖼️ Fast image recognition using perceptual image hashing
- 🎮 Supports original consoles connected through capture cards
- 🕹️ Supports emulators such as PCSX2, DuckStation, Dolphin, RetroArch, and more
- 🖥️ Works with Display Capture, Window Capture, and Game Capture in OBS
- ⚡ Lightweight and easy to configure

---

## Requirements

Before running Retro Presence, make sure you have:

- Python 3.14 or newer
- OBS Studio
- OBS WebSocket enabled
- Discord Desktop

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DiegoBeltre/Retro-Presence.git
cd Retro-Presence
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## OBS Configuration

Retro Presence communicates with OBS using the built-in WebSocket server.

Before running the application:

1. Open **OBS Studio**.
2. Navigate to **Tools → WebSocket Server Settings**.
3. Enable the WebSocket server.
4. Set the password to **123456** (recommended).
5. Make sure your OBS capture source is named **PS2 Capture**.

### Using Your Own Password

If you prefer to use your own WebSocket password:

1. Open `Capture.py`.
2. Replace the password value with your own.

Example:

```python
password = "YOUR_OBS_WEBSOCKET_PASSWORD"
```

The password in `Capture.py` must exactly match the password configured in OBS.

> **Note:** The pre-built `Retro Presence.exe` is compiled using the default password (`123456`). If you use a different password, you must either run `Main.py` directly or rebuild the executable.

---

## Running

Using the default password:

```
Retro Presence.exe
```

Using a custom password:

```bash
python Main.py
```

---

## Notes

- OBS Studio must be running.
- Discord Desktop must be running.
- Your capture source must be named **PS2 Capture**.
- The game must be visible in the configured OBS source.
- Game detection is performed using perceptual image hashes stored in the included database.

---

## Supported Setups

Retro Presence works with virtually any retro gaming setup that can be displayed in OBS, including:

- Original consoles connected through HDMI or analog capture cards
- PCSX2
- DuckStation
- Dolphin
- RetroArch
- Other retro emulators
- Any retro game mirrored into OBS using Display Capture, Window Capture, or Game Capture

If OBS can display it, Retro Presence can detect it.

---

## Limitations

Discord Rich Presence image assets are managed through the Discord Developer Portal.

While anyone can contribute improvements to the game detection database, only the owner of the Discord application can upload new Rich Presence image assets. Because of this, adding support for new games requires both a new image hash and a corresponding Discord asset.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.