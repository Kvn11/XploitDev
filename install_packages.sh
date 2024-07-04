#/usr/bin/bash

# General stuff required
sudo apt update
sudo apt install -y \
python3 python3-pip \
zsh \
bc binutils bison dwarves flex gcc git gnupg2 gzip libelf-dev libncurses5-dev libssl-dev make openssl pahole perl-base rsync tar xz-utils \
tmux \
vim \
gdb

# Setup qemu:
sudo apt update
sudo apt install qemu qemu-kvm virt-manager bridge-utils
sudo useradd -g $USER libvirt
sudo useradd -g $USER libvirt-kvm

# Install VsCode:
sudo apt-get install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
sudo apt install apt-transport-https
sudo apt update
sudo apt install code

sudo useradd -g $USER libvirt
sudo useradd -g $USER libvirt-kvm
