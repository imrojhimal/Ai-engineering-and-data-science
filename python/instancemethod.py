class Laptop:
    storage_type="ssd"
    def __init__(self,RAM,storage):
        self.Ram=RAM
        self.storage=storage
    def get_info(self):
        print(f"laptop has {self.Ram} of Ram and storage of {self.storage} storage type is {self.storage_type}")
l1=Laptop("16GB",'512GB')
l2=Laptop('8GB','500GB')
l1.get_info()   
l2.get_info() 