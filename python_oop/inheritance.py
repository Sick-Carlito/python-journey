# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class (Child)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Another derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)        # Calls Animal's __init__
        self.can_fly = can_fly

    def speak(self):
        flying_status = "can fly" if self.can_fly else "can't fly"
        print(f"{self.name} chirps and {flying_status}.")



dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()
