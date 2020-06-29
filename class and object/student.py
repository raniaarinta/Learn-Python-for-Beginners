class Student:

    def __init__(self, name, major,gpa):
        self.name = name
        self.major= major
        self.gpa = gpa
    def honor_role(self):
        if float(self.gpa)>3.75:
            print("student on a honor role")
        else:
            print("student is not on a honor role")
