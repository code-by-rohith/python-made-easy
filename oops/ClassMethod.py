class Students:

    Fees =10000
    def __init__(self, Name, Roll_num, Course,Section):
        self.Name = Name
        self.Roll_num = Roll_num
        self.Course = Course
        self.Section = Section

    def dep1(self):
        return f"{self.Name} - {self.Roll_num} - {self.Course} - {self.Section} - {self.Fees}"

    def dep2(self):
        return f"{self.Name} - {self.Roll_num} - {self.Course} - {self.Section} - {self.Fees}"

    @classmethod
    def change_fees(cls, new_fees):
        cls.Fees = new_fees


# Create instances of the Students class
stu = Students("Hari", '555', 'MCA',  "A")
stu1 = Students("Rohan", '500', 'MCA', "B")

stu.change_fees("800000")

print(stu.dep1())
print(stu1.dep2())

Name, Roll_num, Course, Section ="Rohith,777,MBA,A ".split(",")
stu2=Students(Name, Roll_num, Course,Section)
print(stu2.Name)