#!/bin/bash
# Install htop from source (configure/make workflow)

sudo apt update
sudo apt install -y git autoconf automake build-essential libncursesw5-dev

git clone https://github.com/htop-dev/htop.git
cd htop

./autogen.sh
./configure --prefix=/usr/local
make -j$(nproc)
sudo make install

# Verify
htop --version
which htop

# To uninstall: cd htop && sudo make uninstall

