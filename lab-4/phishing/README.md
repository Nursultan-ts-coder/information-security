# Lab 4 — Phishing Simulation (Ethical Use Only)

This lab demonstrates how phishing works in a controlled environment to build awareness. Do not deploy or use this code to target real users or services.

## Safety & Ethics

- Run locally only; never expose to the public internet.
- Test with consent (e.g., your own accounts or dummy data).
- Do not use real credentials; never commit secrets to source control.
- Use environment variables or test-only SMTP servers for any email testing.

## Contents

- `server.py` — local Flask server to render a mock login page and capture submitted data to `login_data.txt`.
- `instagram-login.html` — mock login page used by the server.
- `email-template.html` — HTML email template used for awareness demonstrations.
- `mail.py` — example script to send an awareness email (configure safely before use).
- `login_data.txt` — local file where submitted data is stored (created automatically).

## Prerequisites

- Python 3.x
- VS Code (recommended) with Python extension
- Project dependencies from the repository root `requirements.txt`

## Setup

Use the project’s virtual environment for consistency. If it doesn’t exist yet, create `jupyter-env`:

```bash
# From the repository root
python3 -m venv jupyter-env
source jupyter-env/bin/activate
pip install -r requirements.txt
```

In VS Code, select the interpreter at `jupyter-env/bin/python` (Command Palette → “Python: Select Interpreter”).

## Run the Local Server (Awareness Demo)

Start the mock site and interact locally:

```bash
# From this folder: labs/lab-4/phishing
python server.py
```

- Opens a local server on http://localhost:8000
- Visit http://localhost:8000/instagram-login to view the mock page
- Submissions are written to `login_data.txt` in this folder

Only submit dummy data for testing. Delete `login_data.txt` after your demo:

```bash
rm -f login_data.txt
```

Example environment setup and run:

```bash
python mail.py
```
