"""
    Bridge pattern
"""
from abc import ABC


class Shape(ABC):   # Abstraction
    def __init__(self, color):
        self.color = color

    def show(self):
        pass


class Circle(Shape):    # Refined Abstraction
    def show(self):
        self.color.paint(self.__class__.__name__)


class Square(Shape):    # Refined Abstraction
    def show(self):
        self.color.paint(self.__class__.__name__)


class Color(ABC):       # Implementation
    def paint(self, name):
        pass


class Blue(Color):      # Concrete Implementation
    def paint(self, name):
        print(f"this is a {self.__class__.__name__} {name}")


class Red(Color):       # Concrete Implementation
    def paint(self, name):
        print(f"this is a {self.__class__.__name__} {name}")


red = Red()
circle = Circle(red)
circle.show()
