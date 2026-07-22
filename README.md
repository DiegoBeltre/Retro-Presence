# Retro Presence

Retro Presence is a Python application that automatically detects the retro game currently displayed in OBS Studio and updates your Discord Rich Presence in real time.

Using image hashing, the application compares the current OBS capture against a database of known game screenshots and displays the matching title on your Discord profile.

---

## Features

* 🎮 Automatic retro game detection
* 📺 OBS Studio integration via WebSocket
* 💬 Discord Rich Presence support
* 🖼️ Fast image recognition using perceptual image hashing
* ⚡ Lightweight and easy to configure

---

## Requirements

Before running the application, make sure you have:

* Python 3.14 or newer
* OBS Studio
* OBS WebSocket enabled
* Discord Desktop

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

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

Install all required dependencies:

```bash
pip install -r requirements.txt
```

---

## OBS Configuration

Retro Presence communicates with OBS through the OBS WebSocket server.

Before running the application:

1. Open **OBS Studio**.
2. Navigate to **Tools → WebSocket Server Settings**.
3. Make sure the WebSocket server is enabled.
4. You can use your own password or set the WebSocket password to 123456
5. Make sure the capture source in OBS is named PS2 Capture.

IF YOU USE YOUR OWN PASSWORD
1. Open `Capture.py`.
2. Replace the password value with your own OBS WebSocket password.

Example:

```python
password = "YOUR_OBS_WEBSOCKET_PASSWORD"
```

If the password does not match the one configured in OBS, Retro Presence will be unable to connect. 
Note that Retro Presence.exe will break if you use your own password unless you refactor it.

---

## Running

Start the application with Retro Presence.exe or if useing your own password run Main.py

## Notes

* OBS Studio must be running.
* Discord Desktop must be running.
* The game must be visible in the configured OBS source.
* Game detection relies on the included image hash database.

---

## Limitations

Discord Rich Presence image assets are managed by the Discord application associated with this project.

While anyone can use or modify the project, only the owner of the Discord application can add or update Rich Presence image assets. Because of this, support for new games requires updates to the Discord application assets in addition to the detection database.

