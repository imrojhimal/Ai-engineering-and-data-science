class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa
s1=Student("himal",9.0)
s2=Student("boss",2.0)
s3=Student("Hasan",4.0)
print(f'{s1.name} has a cgpa of {s1.get_cgpa()}')
print(s2.name)

