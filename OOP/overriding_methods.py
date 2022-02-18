class Animal:
    def __init__(self, name='Name', sound="Grrrr"):
        self.name = name
        self.sound = sound

    def make_noise(self):
        print("{} says, {}".format(self.name, self.sound))


class Cat(Animal):
    def __init__(self, name='Default'):
        super().__init__(name)


pet_cat = Cat()
pet_cat.make_noise()  # Rachel says, Meow!

