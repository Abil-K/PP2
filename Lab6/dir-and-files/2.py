#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path

import os


def check_path_access(path):
    exists = os.path.exists(path)

    if exists:
        readable = os.access(path, os.R_OK)
        print(f"Readable: {readable}")

        writable = os.access(path, os.W_OK)
        print(f"Writable: {writable}")

        executable = os.access(path, os.X_OK)
        print(f"Executable: {executable}")
    else:
        print("Path does not exist")