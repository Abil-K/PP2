#Write a Python program to write a list to a file.

def writeList(file, list):

    with open(file, 'w') as f:
       for item in list:
           file.write(f"{item}\n")