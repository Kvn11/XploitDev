#/usr/bin/bash

# General stuff required
sudo apt update
sudo apt install -y \
python3 python3-pip \
bc binutils bison dwarves flex gcc git gnupg2 gzip libelf-dev libncurses5-dev libssl-dev make openssl pahole perl-base rsync tar xz-utils \
tmux \
gdb

# Setup qemu:
sudo apt update
sudo apt install qemu qemu-kvm virt-manager bridge-utils
sudo useradd -g $USER libvirt
sudo useradd -g $USER libvirt-kvm

sudo useradd -g $USER libvirt
sudo useradd -g $USER libvirt-kvm
