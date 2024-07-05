#!/usr/bin/bash

USER="jp3g"

# General stuff required
sudo apt update
sudo apt install -y \
python3 python3-pip python3-venv \
bc binutils bison dwarves flex gcc git gnupg2 gzip libelf-dev libncurses5-dev libssl-dev make openssl dwarves perl-base rsync tar xz-utils \
libguestfs-tools \
tmux \
gdb

# Setup qemu:
sudo apt update
sudo apt -y install qemu qemu-kvm bridge-utils
