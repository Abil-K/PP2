#Define a class which has at least two methods: getString: 
#to get a string from console input printString: to print the string in upper case.

class Upper:
    def __init__(task1):
        task1.string=""
    def getString(task1):
        task1.string=input()
    def printString(task1):
        print(task1.string.upper())

x = Upper()
x.getString()
x.printString()