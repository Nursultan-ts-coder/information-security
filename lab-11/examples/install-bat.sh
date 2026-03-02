#!/bin/bash
# Install bat from source (Rust/Cargo compilation)

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source ~/.cargo/env

# Clone and build
git clone https://github.com/sharkdp/bat.git
cd bat
cargo build --release

# Install
sudo cp target/release/bat /usr/local/bin/

# Verify
bat --version
which bat

# Usage: bat file.txt (cat with syntax highlighting)
