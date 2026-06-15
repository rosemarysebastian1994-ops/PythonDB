# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#     @abstractmethod
#     def apply_brake(self):
#         pass
#     @abstractmethod
#     def accelerate(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Start the engine in car")
#     def stop(self):
#         print("Stop the engine in car")
#     def apply_brake(self):
#         print("Apply the brake in the car")
#     def accelerate(self):
#         print("Apply accelerator in the car")
# c = Car()
# c.start()
# c.stop()
# c.apply_brake()
# c.accelerate()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getarea(self):
        pass
    @abstractmethod
    def getperimeter(self):
        pass

class Circle(Shape):
    def __init__(self):
        self.radius = int(input("Enter the radius:"))
    def getarea(self):
        print("The area is", 3.14*(self.radius**2))
    def getperimeter(self):
        print("The perimeter is", 2*3.14*self.radius)

class Rectangle(Shape):
    def __init__(self):
        self.l = int(input("Enter the length: "))
        self.b = int(input("Enter the breadth: "))
    def getarea(self):
        print("The area is", self.l*self.b)
    def getperimeter(self):
        print("The perimeter is", 2*(self.l + self.b))

c = Circle()
c.getarea()
c.getperimeter()
d = Rectangle()
d.getarea()
d.getperimeter()