class Animal:
    def __init__(self, name):
        self.name = name
    def action(self):
        print("{} Афшкн tail. Awwww".format(self.name))


class Dog(Animal):
    def action(self):
        # super().action()
        print("{} wags tail. Awwww".format(self.name))


class Wolf(Animal):
    def action(self):
        # super().action()
        print("{} bites. OUCH!".format(self.name))


class Hybrid(Dog, Wolf):
    def action(self):
        super().action()
        Wolf.action(self)


my_pet = Hybrid("Fluffy")
my_pet.action()  # Fluffy wags tail. Awwww
# Fluffy bites. OUCH!