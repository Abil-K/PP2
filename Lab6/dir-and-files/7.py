#Write a Python program to copy the contents of a file to another file

def copy(source, destinatioin):

    with open(source, "r") as src:
        with open(destinatioin, "w") as dest:
            for line in src:
                dest.write(line)