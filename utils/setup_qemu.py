import requests
import os
from loguru import logger
import argparse
from urllib.request import urlretrieve
import subprocess

DEFAULT_ROOTFS_URL = "https://cloud-images.ubuntu.com/minimal/releases/noble/release-20240618/ubuntu-24.04-minimal-cloudimg-amd64.img"

def download_file(url, directory):
    filename = url.split("/")[-1]
    file_path = os.path.join(directory, filename)
    
    f, headers = urlretrieve(DEFAULT_ROOTFS_URL, file_path)
    logger.info(f"{f} was successfully downloaded.")
    return file_path
    
def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")
        else:
            logger.info(f"Using directory: {directory}")
        
        return True
    
    except OSError as e:
        logger.error(f"Error creating directory {directory}: {e}")
        return False
    
def configure_rootfs(rootfs_path, ssh_pub, modules_path, root_pass="root", user_pass="pwn", users=["pwn"], shell="/bin/bash"):
    
    # TODO: Add abilityt to read configuration from file
    
    command = [
        "virt-customize",
        "-a", rootfs_path,
        "--run-command", "apt-get update",
        "--install", "ssh-server",
        "--install", "vim",
        "--run-command", "systemctl enable ssh",
        "--root-password", f"password:{root_pass}",
        "--ssh-inject", f"root:file:{ssh_pub}",
    ]
    
    for usr in users:
        # Create a new user
        command.extend([
            "--run-command", f"useradd -m -s /bin/bash {usr}"
            ])
        
        # TODO: Give ability to set individual passwords.
        command.extend([
            "--password", f"usr:password:{user_pass}"
            ])
        
        # Add ssh pub key to user:
        command.extend([
            "--ssh-inject", f"{usr}:file:{ssh_pub}"
        ])
        
    command.extend([
        "--copy-in", f"{modules_path}:/lib/modules"
    ])
    
    result = subprocess.run(command, capture_output=True, text=True)

def main(directory, ssh_key, modules_path):
    if not create_directory(directory):
        logger.error("Failed to create or access directory {directory}")
        return
    
    logger.info("Downloading default cloud image rootfs, this might take some time.")
    downloaded_file = download_file(DEFAULT_ROOTFS_URL, directory)
    if downloaded_file:
        logger.info("Configuring image...")
    else:
        logger.error("Failed to set up environment")
        return
    
    configure_rootfs(
        rootfs_path=downloaded_file,
        ssh_pub=ssh_key,
        modules_path=modules_path,
        )
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup kernel exploitation environment for linux using qemu.")
    
    parser.add_argument("-d", "--dir", type=str, required=True,
                        help="Directory to setup the environment in.")
    parser.add_argument("-i", "--ssh_key", type=str, required=True,
                        help="Path to the public ssh key that will be used to login for all users.")
    parser.add_argument("-m", "--modules", type=str, required=True,
                        help="Path to the compiled modules you want to use")
    
    args = parser.parse_args()
    
    # TODO: Add ability to do download + configure, or just configure
    
    main(
        args.dir,
        args.ssh_key,
        args.modules
        )