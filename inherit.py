class Employee:
    start="8 a.m"
    end="6 p.m"
class teacher(Employee):
    salary=30000
    def __init__(self,sub):
        self.subject=sub
t1=teacher("Physics")
print(t1.subject,t1.start)