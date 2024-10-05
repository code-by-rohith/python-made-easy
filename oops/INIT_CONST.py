class Marks:

    def __init__(self):
        self.pi = 3.142

    def __del__(self):
        print("deleted", self)

    def rajesh(self):
        value1 = 6
        value2 = 8
        answer = value1 * value2 * self.pi
        print("rajesh:", answer)

    def kumar(self):
        value1 = 89
        value2 = 75
        answer = value1 * value2 * self.pi
        print("kumar:", answer)


obj1 = Marks()
obj1.rajesh()
obj1.kumar()

