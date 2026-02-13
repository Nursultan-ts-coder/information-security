
# Lab 13. Keylogger

## Overview
Keylogging is the monitoring of keyboard input, often without user knowledge. This lab demonstrates keylogger implementation on Ubuntu systems using Python.

## Types of Keyloggers
- **Software Keyloggers**: Programs installed on systems to record keystrokes at application, OS, or kernel level
- **Hardware Keyloggers**: Physical devices (USB dongles, keyboard connectors) that intercept keystrokes

## Uses
- **Legitimate**: Employee monitoring, child safety, security research
- **Malicious**: Stealing passwords, credit card details, and personal data via malware distribution

## Implementation

### Setup
```bash
mkdir keylogger && cd keylogger
touch main.py
pip install pynput
```

### Key Functions
- `on_key_press()`: Logs each keystroke to console
- `on_key_release()`: Handles Enter/Space for file writing; Escape to stop logging
- `write_to_file()`: Writes filtered keystrokes to `log.txt`, excluding special keys

### Running the Script
```bash
python main.py
```

Set timeout to 10 seconds for testing. The script logs all keystrokes and saves them to `log.txt`.

## Task
Modify the script to send `log.txt` data to an API endpoint for remote storage instead of storing locally.
