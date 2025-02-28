#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.


import os


def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")

        directory, filename = os.path.split(path)

        print(f"Directory: {directory}\n"
              f"Filename: {filename}")
    else:
        print(f"'{path}' does not exist.")