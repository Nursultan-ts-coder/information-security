# Project Setup: VS Code + Jupyter Extension

This guide shows how to install the Jupyter extension in VS Code and set up the Python environment and requirements for these labs on macOS.

## Requirements

- VS Code (latest)
- Python 3.x
- VS Code extensions: Python (Microsoft) and Jupyter (Microsoft)
- A Python virtual environment is provided at `jupyter-env/`
- Project dependencies listed in `requirements.txt`

## Install VS Code Extensions

- Open VS Code → Extensions (left sidebar).
- Search and install:
  - Python — Publisher: Microsoft
  - Jupyter — Publisher: Microsoft
- Optional CLI (if `code` command is available):

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

## Configure Python Environment

Use the provided virtual environment to ensure consistent packages and kernels.

```bash
# From the repository root
source jupyter-env/bin/activate
pip install -r requirements.txt
```

### If `jupyter-env/` does not exist (gitignored)

Create a new Python virtual environment named `jupyter-env` and install dependencies:

```bash
# From the repository root
python3 -m venv jupyter-env
source jupyter-env/bin/activate
pip install -r requirements.txt
```

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
