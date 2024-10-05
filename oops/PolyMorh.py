
class Data:
    def __init__(self):
        self.childage = 12
        self.fatherage = 32

class Father(Data):

    def speak(self):
        return f"I am the father.My age is {self.fatherage}"

class Child(Father):

    def speak(self):

        return f"I am the child. My age is {self.childage}"

father_instance = Father()
child_instance = Child()

# Calling the speak method
print(father_instance.speak())
print(child_instance.speak())
