#!/bin/bash
# Install jq from source (autoreconf/configure workflow)

sudo apt update
sudo apt install -y git build-essential autoconf automake libtool

git clone https://github.com/jqlang/jq.git
cd jq
git submodule update --init

autoreconf -i
./configure --prefix=/usr/local --disable-maintainer-mode
make -j$(nproc)
sudo make install

# Verify
jq --version
which jq

# Usage: echo '{"name":"John"}' | jq .name
