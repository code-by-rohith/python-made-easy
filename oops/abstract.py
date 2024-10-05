from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
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

