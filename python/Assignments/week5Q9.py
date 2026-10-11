class herbivoore:
    food="green grass"
    def diet(self):
        print(f"Herbivore animal eats {herbivoore.food}")
class carnivore:
    food="meat"
    def diet(self):
        print(f"carnivore animal eats {carnivore.food}")
class omnivore(herbivoore,carnivore):
    def diet(self):
       print(f"they eats {herbivoore.food} and {carnivore.food}") 
class bear(omnivore):
   def diet(self):
       super().diet()
       print("bear also love fish and barries too")
b=bear()
b.diet()
