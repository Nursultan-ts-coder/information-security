# Lab 11: Installing Packages from Source

## Why Install from Source?

| Reason                   | Description                                       |
| ------------------------ | ------------------------------------------------- |
| **Latest Version**       | Get newest features/fixes before they're packaged |
| **Customization**        | Enable/disable features, custom install paths     |
| **Optimization**         | Compile for your specific hardware                |
| **No Package Available** | Software not in your distro's repositories        |

---

## Key Concepts

### Build Tools

| Tool          | Purpose                              |
| ------------- | ------------------------------------ |
| `gcc` / `g++` | C/C++ compilers                      |
| `make`        | Automates compilation using Makefile |
| `cmake`       | Modern build system generator        |
| `autoconf`    | Generates configure scripts          |
| `./configure` | Checks dependencies, prepares build  |

### Common Dependencies Package

```bash
# Install build essentials (Debian/Ubuntu)
sudo apt install build-essential git curl wget

# Includes: gcc, g++, make, libc-dev
```

---

## Installation Methods

### Method 1: Classic (configure/make/make install)

```bash
# 1. Download source
wget https://example.com/software-1.0.tar.gz

# 2. Extract
tar -xvzf software-1.0.tar.gz
cd software-1.0

# 3. Configure (check dependencies, set options)
./configure

# 4. Compile
make

# 5. Install (usually to /usr/local/)
sudo make install
```

### Method 2: CMake (Modern Projects)

```bash
# 1. Clone repository
git clone https://github.com/example/project.git
cd project

# 2. Create build directory (out-of-source build)
mkdir build && cd build

# 3. Generate Makefiles
cmake ..

# 4. Compile
make

# 5. Install
sudo make install
```

### Method 3: Rust Projects (Cargo)

```bash
# 1. Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env

# 2. Clone and build
git clone https://github.com/example/rust-project.git
cd rust-project
cargo build --release

# 3. Install binary
sudo cp target/release/binary /usr/local/bin/
```

> **Note:** Python scripts (pip install, setup.py) do NOT count as "install from source"
> because there's no compilation step. Use C/C++/Rust projects for this lab.

---

## Important Commands Reference

### Extraction Commands

| File Extension     | Command                  |
| ------------------ | ------------------------ |
| `.tar.gz` / `.tgz` | `tar -xvzf file.tar.gz`  |
| `.tar.bz2`         | `tar -xvjf file.tar.bz2` |
| `.tar.xz`          | `tar -xvJf file.tar.xz`  |
| `.zip`             | `unzip file.zip`         |

### tar flags explained:

- `x` = extract
- `v` = verbose (show files)
- `z` = gzip compression
- `j` = bzip2 compression
- `J` = xz compression
- `f` = file (must be last flag)

### Make Commands

| Command                    | Purpose                               |
| -------------------------- | ------------------------------------- |
| `make`                     | Compile the project                   |
| `make -j4`                 | Compile with 4 parallel jobs (faster) |
| `make clean`               | Remove compiled files                 |
| `make install`             | Install to system                     |
| `make uninstall`           | Remove installed files (if supported) |
| `make check` / `make test` | Run tests                             |

### Configure Options (common)

```bash
# Install to custom location
./configure --prefix=/opt/myapp

# Enable/disable features
./configure --enable-feature --disable-other

# Show all options
./configure --help
```

---

## Real-World Example 1: Installing htop from Source (RECOMMENDED)

htop is an interactive process viewer.

```bash
# 1. Install dependencies
sudo apt update
sudo apt install git autoconf automake build-essential libncursesw5-dev

# 2. Clone repository
git clone https://github.com/htop-dev/htop.git
cd htop

# 3. Generate configure script
./autogen.sh

# 4. Configure
./configure

# 5. Compile
make

# 6. Install
sudo make install

# 7. Verify
htop --version
```

This demonstrates the **full compilation workflow**:

1. `./autogen.sh` - Generate configure script from autoconf files
2. `./configure` - Check system, find dependencies, create Makefile
3. `make` - Compile C source code into binary
4. `make install` - Copy compiled binary to system

---

## Real-World Example 2: Installing jq from Source

jq is a lightweight JSON processor written in C.

```bash
# 1. Install dependencies
sudo apt update
sudo apt install git build-essential autoconf automake libtool

# 2. Clone repository
git clone https://github.com/jqlang/jq.git
cd jq
git submodule update --init

# 3. Generate configure script
autoreconf -i

# 4. Configure
./configure --prefix=/usr/local

# 5. Compile
make -j$(nproc)

# 6. Install
sudo make install

# 7. Verify
jq --version
```

---

## Real-World Example 3: Installing bat (cat replacement) - Rust

bat is a cat clone with syntax highlighting.

```bash
# 1. Install Rust (required for bat)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env

# 2. Clone repository
git clone https://github.com/sharkdp/bat.git
cd bat

# 3. Build with Cargo (Rust's package manager)
cargo build --release

# 4. Install binary manually
sudo cp target/release/bat /usr/local/bin/

# 5. Verify
bat --version
```

---

## What Does NOT Count as "Install from Source"

| Tool Type          | Example      | Why it doesn't count                            |
| ------------------ | ------------ | ----------------------------------------------- |
| Python scripts     | yt-dlp, tldr | No compilation - just copies .py files          |
| Bash scripts       | neofetch     | No compilation - just copies .sh files          |
| Pre-built binaries | fzf          | Downloads compiled binary, no local compilation |

---

## Troubleshooting

### Common Errors and Solutions

| Error                                                    | Cause                 | Solution                           |
| -------------------------------------------------------- | --------------------- | ---------------------------------- |
| `command not found: make`                                | make not installed    | `sudo apt install build-essential` |
| `configure: error: C compiler cannot create executables` | Missing compiler      | `sudo apt install gcc`             |
| `error: dependency X not found`                          | Missing library       | `sudo apt install libX-dev`        |
| `Permission denied`                                      | Need root for install | Use `sudo make install`            |
| `make: *** No targets specified`                         | No Makefile           | Run `./configure` or `cmake` first |

### Finding Dependencies

```bash
# Search for package providing a file
apt-file search missing_header.h

# Install apt-file first
sudo apt install apt-file
sudo apt-file update
```

---

## Cleaning Up / Uninstalling

### If Makefile supports uninstall:

```bash
cd /path/to/source
sudo make uninstall
```

### Manual removal:

```bash
# Check what was installed
cat install_manifest.txt  # If exists

# Or check common locations
ls /usr/local/bin/
ls /usr/local/lib/
```

### Remove source directory:

```bash
cd ..
rm -rf software-directory
```

---

## Best Practices

1. **Keep source directories** - You'll need them to uninstall
2. **Use `--prefix`** - Install to `/opt/appname` for easy removal
3. **Check for package first** - `apt search appname` before compiling
4. **Read README/INSTALL** - Each project may have specific requirements
5. **Use `-j$(nproc)`** - Speeds up compilation: `make -j$(nproc)`

---

## Quick Reference Card

```bash
# Standard workflow
git clone <repo>
cd <project>
./configure --prefix=/usr/local  # or cmake ..
make -j$(nproc)
sudo make install

# Verify
which <command>
<command> --version

# Uninstall
cd /path/to/source
sudo make uninstall
```
