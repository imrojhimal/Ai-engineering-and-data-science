class student:
    def __init__(self,name,rollno,marks):
        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
    def setmarks(self,newmarks):
        self.__marks=newmarks

    def getmarks(self):
        return self.__marks
s1=student("Imroj Ahasan",21,89)
s1.setmarks(300)
print(s1._student__name,s1.getmarks())