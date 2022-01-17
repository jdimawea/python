class Ninja:


    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.name = first_name
        self.name = last_name
        self.treats = treats
        self.food = pet_food
        self.pet = pet


    def walk(self):
        self.pet.play()
        return self


    def feed(self):
        self.pet.eat()
        return self


    def bathe(self):
        self.pet.noise()
        return self


class Pet:


    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100


    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping")
        return self


    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating")
        return self


    def play(self):
        self.health += 5
        print(f"{self.name} is walking")
        return self


    def noise(self):
        print("Woof")
        return self


john = Ninja("Jonathan", "Dimawea", "Beef Jerky", "Steak", Pet("Zezal", "Dog", "shake hands"))


john.walk().feed().bathe()
