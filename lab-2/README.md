# Lab 2

Friendly guide for working with the Lab 2 notebooks in this folder.

## Overview

This lab contains several Jupyter notebooks with small tasks and examples. You can run them directly in VS Code using the Jupyter extension (recommended), or via JupyterLab/Notebook.

## Contents

- sample.ipynb — example notebook to verify your environment
- task-1.ipynb
- task-2.ipynb
- task-3.ipynb
- task-4.ipynb
- words.txt — text data used by some tasks
- test_dir/ — directory used by filesystem tasks

## Prerequisites

- Python 3.x installed on your machine
- VS Code with the Python and Jupyter extensions
- Optional: project dependencies from the root requirements.txt

## Quick Start (VS Code)

1. Open the folder `labs/lab-2/` in VS Code.
2. Install extensions: Python (Microsoft) and Jupyter (Microsoft).
3. Select the interpreter from `jupyter-env`:

- Use the Command Palette → “Python: Select Interpreter” → choose the interpreter under `labs/jupyter-env/bin/python`.

4. Open any notebook (e.g., `task-1.ipynb`) and select the kernel matching the selected interpreter.
5. Run cells with the Run button or “Run All”.

## Tips

- Keep `words.txt` and `test_dir/` paths unchanged relative to this folder.
- In VS Code, use “Restart Kernel and Run All” after changing imports or the interpreter.
- Prefer clear cell order: imports → config → data → processing → results.

## Troubleshooting

- VS Code can’t find the kernel: re-run “Python: Select Interpreter” and pick `labs/jupyter-env/bin/python`, then re-open the notebook.
- Missing packages: install from the root `requirements.txt` or inside a cell:
  ```python
  %pip install <package>
  ```
- Trust prompts: if VS Code asks to trust the workspace/notebook, choose “Yes” to enable execution.
