#Define a class named Rectangle which inherits from Shape class from task 2. 
#Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Shape:
    def __init__(task3):
        task3.area = 0
class Rectangle(Shape):
    def __init__(task3, width, length):
        super().__init__()
        task3.width = width
        task3.length = length
    def getParameters(task3):
        task3.width = int(input("width: "))
        task3.length = int(input("lenght: "))
    def printArea(task3):
        task3.area = task3.width * task3.length
        return task3.area

a = Rectangle(0, 0)
a.getParameters()
print("Area:", a.printArea())