class student:
    def __init__(self,age):
        self._age=age #protected but not completely secured
s=student(20)
print(s._age) #accessible by the underscore not secured 


        