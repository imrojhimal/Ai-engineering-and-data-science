class Laptop:
    def __init__(self,RAM,storage):
        self.Ram=RAM
        self.storage=storage
    @classmethod
    def getstor(cls):
        print("ssd")
        
    def get_info(self):
        print(f"laptop has {self.Ram} of Ram and storage of {self.storage} storage type is {self.storage_type}")
    @staticmethod
    def calc_discount(price,discount):
        finalprice=price-((price*discount)/100)
        return finalprice


l1=Laptop("16GB",'512GB')
l2=Laptop('8GB','500GB')
l1.getstor()
print(l1.calc_discount(4000,10))