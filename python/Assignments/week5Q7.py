class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address
        
        if age is None and address is None:
            print("Constructor 1 logic executed: Created Person with Name only.")
        elif address is None:
            print("Constructor 2 logic executed: Created Person with Name + Age.")
        else:
            print("Constructor 3 logic executed: Created Person with Name + Age + Address.")

    def display_info(self):
        
        age_display = self.age if self.age is not None else "Not Provided"
        address_display = self.address if self.address is not None else "Not Provided"
        print(f"Name: {self.name} | Age: {age_display} | Address: {address_display}\n")

person1 = Person("Alice")
person1.display_info()
person2 = Person("Bob", 25)
person2.display_info()
person3 = Person("Charlie", 30, "123 Main St, New York")
person3.display_info()
