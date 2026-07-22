# Retro Presence

Automatic Discord Rich Presence for retro games using OBS video capture and perceptual image hashing.

No machine learning.

No game database.

Just screenshots.

---

## Requirements

- Windows
- Discord Desktop
- OBS Studio
- OBS WebSocket

---

## OBS Setup

Retro Presence expects the following OBS configuration:

Source Name:

PS2 Capture

WebSocket Settings:

Host: localhost
Port: 4455
Password: 123456

Enable WebSocket:

Tools
→ WebSocket Server Settings
→ Enable WebSocket Server

IMPORTANT:

The OBS source MUST be named exactly:

PS2 Capture

If the source name is different, Retro Presence will not work.

---

## Running

Launch:

Retro Presence.exe

or

Main.py

---

## Adding Games

Place screenshots of the games title screen inside:

LibAssets/

Filename format:

GAME_NAME111CONSOLE.png

Examples:

RESIDENT_EVIL_4111PlayStation 2.png

Final_Fantasy_X111PlayStation 2.png

Destroy_All_Humans111PlayStation 2.png

MonkeyBall111GameCube.png

Gears_of_war111Xbox 360.png

Restart Retro Presence after adding new screenshots.

---

## Filename Parsing

Example:

RESIDENT_EVIL_4111PlayStation 2.png

Becomes:

Game:
Resident Evil 4

Console:
PlayStation 2

Displayed in Discord:

Resident Evil 4
PlayStation 2

---

## Detection Pipeline

OBS Video Feed
↓
Screenshot Capture
↓
Perceptual Hash
↓
Library Comparison
↓
Best Match
↓
Discord Rich Presence

---

## Library Structure

LibAssets/

├── RESIDENT_EVIL_4111PlayStation 2.png

├── RESIDENT_EVIL_4_MENU111PlayStation 2.png

├── RESIDENT_EVIL_4_CASTLE111PlayStation 2.png

├── Final_Fantasy_X111PlayStation 2.png

├── Destroy_All_Humans111PlayStation 2.png

Multiple screenshots can represent the same game.

Adding more screenshots generally improves detection reliability.

---

## Discord Assets

Games with configured Discord assets will display cover art.

Games without configured assets will automatically fall back to the default console icon.

---

## Troubleshooting

### OBS Connection Failed

Verify:

- OBS is running
- WebSocket is enabled
- Port is 4455
- Password is 123456

### Source Not Found

Verify the source is named exactly:

PS2 Capture

### Discord Not Updating

Verify:

- Discord Desktop is running
- Retro Presence.exe is running

### Game Not Detected

Try:

- Adding additional screenshots
- Using gameplay screenshots
- Using screenshots with unique UI elements
- Confirming screenshots are inside LibAssets

---

## Supported Sources

- PlayStation 2
- PSP
- GameCube
- Dreamcast
- Xbox
- Wii
- Emulators
- Capture Cards

If OBS can see it, Retro Presence can attempt to identify it.

---

## Built With

- Python
- OBS WebSocket
- OpenCV
- ImageHash
- PyPresence

Created by Diego Beltre