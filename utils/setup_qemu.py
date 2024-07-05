import requests
import os
from loguru import logger
import argparse
from urllib.request import urlretrieve

DEFAULT_ROOTFS_URL = "https://cloud-images.ubuntu.com/minimal/releases/noble/release-20240618/ubuntu-24.04-minimal-cloudimg-amd64.img"

def download_file(url, directory):
    filename = url.split("/")[-1]
    file_path = os.path.join(directory, filename)
    
    f, headers = urlretrieve(DEFAULT_ROOTFS_URL, file_path)
    logger.info(f"{f} was successfully downloaded.")
    return f
    
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

def main(directory):
    if not create_directory(directory):
        logger.error("Failed to create or access directory {directory}")
        return
    
    logger.info("Downloading default cloud image rootfs")
    downloaded_file = download_file(DEFAULT_ROOTFS_URL, directory)
    if downloaded_file:
        logger.info("Configuring image...")
    else:
        logger.error("Failed to set up environment")
        return
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup kernel exploitation environment for linux using qemu.")
    
    parser.add_argument("-d", "--dir", type=str, required=True,
                        help="Directory to setup the environment in.")
    
    args = parser.parse_args()
    
    main(args.dir)