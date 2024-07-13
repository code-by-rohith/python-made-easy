class vehicle:
    wheels=True
    @property
    def move_forword(self):
        print("Moving  Forword")

class car(vehicle):
    no_of_wheels=4

car1=car()
print(car1.wheels)
print(car1.no_of_wheels)
car1.move_forword