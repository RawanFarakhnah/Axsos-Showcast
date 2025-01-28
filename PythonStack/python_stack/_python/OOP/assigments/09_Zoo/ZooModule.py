from AnimalModule import Lion, Monkey, Bear

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_animal(self, *new_animal):
        for animal in new_animal:
            self.animals.append(animal)
    
    def print_all_info(self):
        print("-"*20, self.name , "-"*20)
        for animal in self.animals:
            animal.display_info()

if __name__ == "__main__":
   zoo = Zoo("John's Zoo")

   lion = Lion(name = "Lion", age = 10, health = 30, happiness = 40, strong_level=10)
   monkey = Monkey(name = "Monkey", age = 4, health = 70, happiness = 70, family_member = 14)
   bear = Bear(name = "Monkey", age = 4, health = 70, happiness = 90, favarite="Hony")

   zoo.add_animal(lion, monkey, bear)
   zoo.print_all_info()
