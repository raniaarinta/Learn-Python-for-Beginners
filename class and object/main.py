from student import Student

student1 = Student("kelly","art","3.9")
student2 = Student("Ken","computer science","4.0")
student3 = Student("Brad","computer science","3.2")
print(student1.name,student1.major,student1.gpa)
student1.honor_role()
print(student2.name,student2.major,student2.gpa)
student2.honor_role()
print(student3.name,student3.major,student3.gpa)
student3.honor_role()
