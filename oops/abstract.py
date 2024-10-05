from abc import ABC, abstractmethod

#overide must in abstract
"""
An abstract class in object-oriented programming is a class that cannot be 
instantiated on its own and serves as a template for other classes. 
It may contain abstract methods—methods that have no implementation in the abstract 
class but must be implemented by its subclasses.
"""

class Vehicle(ABC):

    def start_engine(self):
        """When we don't give the abstract decorator, it means this is a concrete method,
            not an abstract one, and it provides a full implementation that can be used by instances
            of the class or subclasses without requiring them to override it."""
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started!")

    def stop_engine(self):
        print("Engine stopped!")

    def drive(self):
        print("Car is driving!")

my_car = Car()
my_car.start_engine()  # Output: Engine started!
my_car.drive()         # Output: Car is driving!
my_car.stop_engine()   # Output: Engine stopped!

