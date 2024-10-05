
"""
Encapsulation is the concept in programming where data and methods are bundled together within a class,
and access to that data is restricted. It hides the internal details of an
object and only allows interaction through specific methods,
helping to protect and control how the data is used or modified.
"""



class Student:
    def __init__(self, name, roll, marks):
        self.__name = name
        self.__roll = roll
        self.__marks = marks
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_roll(self):
        return self.__roll

    def set_roll(self, roll):
        self.__roll = roll

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def display(self):
        print(f"Name: {self.__name}, Roll No: {self.__roll}, Marks: {self.__marks}")

student = Student(name="Rohith", roll=12345, marks=85)
student.display()

print("\nGetting current name:", student.get_name())
student.set_name("Raj")
print("Updated name:", student.get_name())

print("\nGetting current roll number:", student.get_roll())
student.set_roll(54321)
print("Updated roll number:", student.get_roll())

print("\nGetting current marks:", student.get_marks())
student.set_marks(95)
print("Updated marks:", student.get_marks())

student.set_marks(150)
student.display()
