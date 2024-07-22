class vehicle:
    wheels=True

    @property
    def move_forword(self):
        print("Moving  Forword")

class car(vehicle):
    no_of_wheels=4
class bike(vehicle):
    no_of_wheels=2

car1=car()
print("Wheels : ",car1.wheels)
print("No of wheels :",car1.no_of_wheels)
car1.move_forword
print("")
bike1=bike()
print("wheels : ",bike1.wheels)
print("No of wheels :",bike1.no_of_wheels)
bike1.move_forword


