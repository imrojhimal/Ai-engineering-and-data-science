class Student:
    def __init__(self,gpa):
        self.gpa=gpa
class Teacher:
    def __init__(self,salary):
        self.salary=salary
class TA(Teacher,Student):
    def __init__(self, salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name=name
ta1=TA(30000,9.3,"Imroj")
print(ta1.gpa)