#Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(task2):
        task2.area = 0

class Square(Shape):
    def __init__(task2, length):
        super().__init__()
        task2.length = length
    def getLength(task2):
        task2.length = int(input("side: "))
    def calculateArea(task2):
        task2.area = task2.length * task2.length
        return task2.area
a = Square(0)
a.getLength()
print("Area:", a.calculateArea())