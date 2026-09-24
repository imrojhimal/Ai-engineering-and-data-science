class Employee:
    def designation(self):
        print("employee")
class Teacher(Employee):
    def designation(self):
        print("Teacher")
t=Teacher()
t.designation()