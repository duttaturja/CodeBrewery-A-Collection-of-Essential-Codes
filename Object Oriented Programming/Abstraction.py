#importing libraries
from abc import ABC, abstractmethod

#parent class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

#sub class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.1416 * self.radius ** 2
        print(f"The area is {area}")
    
#sub class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"The area is {area}")
    
#creating instances
circle = Circle(3)
rectangle = Rectangle(3,4)

#calling methods
circle.area()
rectangle.area()