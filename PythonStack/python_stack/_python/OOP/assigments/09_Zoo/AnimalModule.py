#Parent (Master) Class
class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    #Display Animal Info
    def display_info(self):
        print("Name: {0}, Age: {1}, Health Level: {2}, Happiness Level: {3}".format(self.name, self.age,self.health_level, self.happiness_level))

    #Allow to Increase Animal Happiness and Health each by 10
    def feed(self):
        self.happiness_level += 10
        self.health_level += 10

#Child (Slave) Class
class Lion(Animal):
    def __init__(self, name, age, health, happiness, strong_level):
        super().__init__(name, age, health, happiness)
        self.strong_level = strong_level

    def feed(self):
        self.happiness_level *= 2
        self.health_level *= 4

#Child (Slave) Class
class Monkey(Animal):
    def __init__(self, name, age, health, happiness, family_member):
        super().__init__(name, age, health, happiness)
        self.family_member = family_member

    def feed(self):
        self.happiness_level += 12
        self.health_level += 15

#Child (Slave) Class
class Bear(Animal):
    def __init__(self, name, age, health, happiness, favarite):
        super().__init__(name, age, health, happiness)
        self.favarite = favarite

    def feed(self):
        self.health_level = self.happiness_level

if __name__ == "__main__":
   #Create an Instances 
   lion = Lion(name = "Lion", age = 10, health = 30, happiness = 40, strong_level=10)
   monkey = Monkey(name = "Monkey", age = 4, health = 70, happiness = 70, family_member = 14)
   bear = Bear(name = "Monkey", age = 4, health = 70, happiness = 90, favarite="Hony")

   print("Before Feed")
   print(lion.display_info())
   print(monkey.display_info())
   print(bear.display_info())

   lion.feed()
   monkey.feed()
   bear.feed()

   print("\nAfter Feed")
   print(lion.display_info())
   print(monkey.display_info())
   print(bear.display_info())

