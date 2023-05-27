class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self.name = name
        self.hunger = hunger

    def get_name(self):
        return self.name

    def is_hungry(self):
        return self.hunger > 0

    def feed(self):
        self.hunger -= 1

    def talk(self):
        pass

    def special_method(self):
        if isinstance(self, Dog):
            self.fetch_stick()
        elif isinstance(self, Cat):
            self.chase_laser()
        elif isinstance(self, Skunk):
            self.stink()
        elif isinstance(self, Unicorn):
            self.sing()
        elif isinstance(self, Dragon):
            self.breath_fire()


class Dog(Animal):
    def talk(self):
        print("woof woof")

    @staticmethod
    def fetch_stick():
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    @staticmethod
    def chase_laser():
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        self.stink_count = stink_count

    def talk(self):
        print("tsssss")

    @staticmethod
    def stink():
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    @staticmethod
    def sing():
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self.color = color

    def talk(self):
        print("Raaaawr")

    @staticmethod
    def breath_fire():
        print("$@#$#@$")


def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)

    zoo_lst = [dog, cat, skunk, unicorn, dragon]

    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)

    zoo_lst.extend([dog2, cat2, skunk2, unicorn2, dragon2])

    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__, end=" ")
            print(animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        animal.special_method()

    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
