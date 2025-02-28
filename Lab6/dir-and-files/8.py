#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

def delete_file_if_exists(file_path):

    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
                os.remove(file_path)