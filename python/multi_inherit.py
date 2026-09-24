class Employee:
    start="8a.m"
    end="6p.m"
class admin(Employee):
    def __init__(self,role):
       self.role=role
class accoutant(admin):
    def __init__(self,salary, role):
        super().__init__(role)
        self.salary=salary
acc=accoutant(30000,"Charted accountant")
print(acc.salary,acc.role,acc.start,acc.end)