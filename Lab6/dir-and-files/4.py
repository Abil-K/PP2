#Write a Python program to count the number of lines in a text file.

def lines(file):
    stringCount = 0

    with open(file, 'r') as f:
        for line in file:
            stringCount = +1
    return stringCount