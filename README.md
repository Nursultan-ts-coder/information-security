# Information Security Lab Sessions

**Course:** Information Security (COM-424.1) | **University:** American University of Central Asia (AUCA) | **Semester:** Spring 2026 **Student:** Nursultan Lukmanov ID: 14467

## About This Repository

This repository contains hands-on security labs covering 13 different topics, from basic terminal commands to advanced attacks like keylogging and phishing. All work is **for educational purposes only**.

> **⚠️ DISCLAIMER:** This repository contains security lab exercises for **educational purposes only**. Some labs demonstrate potentially harmful techniques to teach defensive security concepts. **Do not use any code for malicious purposes.** Unauthorized access is illegal. Use responsibly and only in authorized environments.

## Lab Overview

| Lab | Topic                             | Key Files                        |
| --- | --------------------------------- | -------------------------------- |
| 1   | Basic Commands & Terminal         | `basic-commands.ipynb`           |
| 2   | Shell Scripting & File Management | `task-*.ipynb`                   |
| 3   | Python Shell Implementation       | `toy_shell.py`                   |
| 4   | Phishing & Social Engineering     | `mail.py`, HTML templates        |
| 5   | User Management                   | `user-management.ipynb`          |
| 6   | File Permissions & Security       | `file-permissions.ipynb`         |
| 7   | Process Scheduling (Cron)         | `crontab.ipynb`                  |
| 8   | Vim Text Editor                   | `vim-essentials.ipynb`           |
| 9   | Package Management                | `index.md`                       |
| 10  | Nginx & Web Configuration         | `nginx-configs/`, `main.py`      |
| 11  | Package Installation from Source  | Installation scripts             |
| 12  | Brute-Force Testing               | `brute-force-server/main.py`     |
| 13  | Keylogging & Data Exfiltration    | `keylogger/main.py`, `server.py` |

## Setup Instructions

### Prerequisites

- Python 3.x
- VS Code (optional, for Jupyter notebooks)
- Jupyter or Jupyter Lab

### Quick Start

```bash
# Activate the virtual environment
source jupyter-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Open Jupyter Lab or Jupyter Notebook
jupyter lab
```

### If Virtual Environment Doesn't Exist

```bash
# Create a new virtual environment
python3 -m venv jupyter-env
source jupyter-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Viewing the Labs

- **Jupyter Notebooks:** Open `.ipynb` files in Jupyter Lab or VS Code with Jupyter extension
- **Python Scripts:** Run with `python filename.py`
- **Configuration Files:** View and configure as needed
- **Documentation:** Read `index.md` files in each lab folder for detailed information

Then, in VS Code, select the interpreter at `jupyter-env/bin/python` via the Command Palette → “Python: Select Interpreter”. The Jupyter extension will detect this environment as a kernel for notebooks.

## Run Notebooks in VS Code

1. Open the folder in VS Code: File → Open Folder → select `labs/` (this directory).
2. Select the Python interpreter:
   - Command Palette → “Python: Select Interpreter” → choose the interpreter at `jupyter-env/bin/python`.
3. Open a notebook (e.g., any file in `lab-2/` with `.ipynb`).
4. Ensure the kernel matches the selected interpreter.
5. Run cells via the Run button or “Run All”.

## Tips

- Keep data and helper files in their original relative paths (e.g., `lab-2/words.txt`, `lab-2/test_dir/`).
- If you change imports or the interpreter, use “Restart Kernel and Run All”.
- You can install missing packages inside a notebook cell:

```python
%pip install <package>
```

## Troubleshooting

- Kernel not found in VS Code: re-run “Python: Select Interpreter” and choose `jupyter-env/bin/python`, then re-open the notebook.
- Missing `code` CLI: enable “Shell Command: Install 'code' command in PATH” from the VS Code Command Palette.
- Extension trust prompts: choose “Yes” to trust the workspace to enable execution.
- If Jupyter isn’t recognized, install:

```bash
pip install jupyterlab
# or
pip install notebook
```

## Bash Kernel for Notebooks

Run pure Bash notebooks or Bash-only cells using a dedicated Jupyter Bash kernel. Install it inside your project environment (`jupyter-env`) so VS Code can discover it.

```bash
# From the repository root
source jupyter-env/bin/activate
pip install bash_kernel
python -m bash_kernel.install
```

### Use in VS Code

- Open a notebook, click the Kernel picker (top-right), and select `Bash`.
- Create a new notebook and choose `Bash` to run only shell commands.

### Quick test (Bash kernel)

Run a cell with:

```bash
echo "Hello from Bash kernel"
uname -a
```

### Alternative: Bash in Python notebooks

If you prefer to stay on the Python kernel, use IPython’s cell magic:

```python
%%bash
echo "Hello via %%bash"
ls -la
```

### Uninstall (optional)

```bash
source jupyter-env/bin/activate
python -m bash_kernel.uninstall
```
