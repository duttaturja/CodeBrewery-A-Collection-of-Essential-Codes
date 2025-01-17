#Open/Close principle
#open for extension closed for modification 

#parent class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
#sub class
class Circle(Shape):
    def __init__(self, radius):
        
        self.radius = radius

    def area(self):
        area = 3.1416 * self.radius ** 2
        print(f"The area of the Circle is {area}")
    
#sub class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"The area of the Rectangle is {area}")
    
#sub class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side ** 2
        print(f"The area of the Square is {area}")

#creating instances
circle = Circle(3)
rectangle = Rectangle(3,4)
square = Square(4)

#calling methods
circle.area()
rectangle.area()
square.area()