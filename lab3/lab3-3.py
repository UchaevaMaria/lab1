from abc import ABC, abstractmethod #используем abctract base class из модуля abc
import math
class Shape(ABC):
    @abstractmethod 
    def area(self): # метод area абстр, означает, что насл shape обяз реал его
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):#задаем параметры
            self.width = width
            self.height = height 
    def area(self):  #реализуем метод area для класса rectangle
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width+self.height) #возвращаем площадь прямоугольника
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2 #герон
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
def print_shape_info(Shape):#опред info приним объект shape
    print("площадь", Shape.area())  
    print("периметр", Shape.perimeter())
#проверка
rectangle = Rectangle(2, 10)
circle = Circle(5)
triangle = Triangle(3, 4, 5)
print_shape_info(rectangle)
print_shape_info(circle)
print_shape_info(triangle)