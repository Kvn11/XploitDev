#!/usr/bin/bash

USER="jp3g"

# General stuff required
sudo apt update
sudo apt install -y \
python3 python3-pip \
bc binutils bison dwarves flex gcc git gnupg2 gzip libelf-dev libncurses5-dev libssl-dev make openssl dwarves perl-base rsync tar xz-utils \
tmux \
gdb

# Setup qemu:
sudo apt update
sudo apt install qemu qemu-kvm virt-manager bridge-utils
sudo usermod -aG libvirt $USER
sudo usermod -aG libvirt-kvm $USER
sudo usermod -aG libvirt-qemu $USER
