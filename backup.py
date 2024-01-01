# When run this script will take the following actions:
# 1. Zip the contents of the specific folder into a zip file with a timestamp
# 2. Copy the zip file to the backup folder

import os
import time
import zipfile
import shutil

backup_to_dropbox = True

folder_source = '/Users/Your Vault Path'
destination = '/Users/Destination Folder For Zip File' # folder must exist
dropbox_path = '/Users/username/Library/CloudStorage/Dropbox/Obsidian Backups' # folder must exist


def create_zip(folder):
    print(f"Creating zip file from {folder}... ")
    # Create the name of the zip file
    zip_name = time.strftime('%Y%m%d%H%M%S') + '.zip'
    # Create the full path of the zip file
    zip_path = os.path.join(destination, zip_name)
    # Create the zip file
    zip_file = zipfile.ZipFile(zip_path, 'w')
    # Walk through the folder and add the files to the zip file
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # Get the full path of the file
            full_path = os.path.join(foldername, filename)
            # Get the relative path to the file
            relative_path = os.path.relpath(full_path, folder)
            # Write the file to the zip file with its relative path
            zip_file.write(full_path, arcname=relative_path, compress_type=zipfile.ZIP_DEFLATED)
    # Close the zip file
    zip_file.close()
    print('Zip file created: ' + zip_path)
    return zip_path

def copy_to_dropbox(zip_path):
    print ('Copying zip file to Dropbox...')
    # Create the full path of the file in the Dropbox folder
    dropbox_zip_path = os.path.join(dropbox_path, os.path.basename(zip_path))
    # Copy the file to the Dropbox folder
    shutil.copy(zip_path, dropbox_zip_path)
    print('Zip file copied to Dropbox: ' + dropbox_zip_path)


zip_path = create_zip(folder_source)
if backup_to_dropbox:
    copy_to_dropbox(zip_path)
