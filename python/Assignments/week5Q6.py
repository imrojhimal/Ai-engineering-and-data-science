from abc import ABC,abstractmethod
class employee:
    def __init__(self,name,base,bonus):
        self.name=name
        self.base=base
        self.bonus=bonus
    @abstractmethod
    def calculatesalary(self):
     pass
class Intern(employee):
   def calculatesalary(self):
      self.total=self.base+(self.base*(self.bonus/100))
      return self.total
class fulltime(employee):
   def calculatesalary(self):
      self.houserent=10000
      self.medical=4500
      self.total=self.base+(self.base*(self.bonus/100))+self.houserent+self.medical
      return self.total
class contact(employee):
   def __init__(self, name, hour, rate):
      super().__init__(name, base=0, bonus=0)
      self.rate=rate
      self.hour=hour
   def calculatesalary(self):
       return self.rate*self.hour

Inemp=Intern("himal",15000,10)
ft=fulltime("Imroj",50000,50)
ct=contact("Tahmid",10,250)
print(Inemp.name,Inemp.calculatesalary())
print(ft.name,ft.calculatesalary())
print(ct.name,ct.calculatesalary())
