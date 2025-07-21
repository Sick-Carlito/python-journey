# Define a class called Person
class Person:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute for name
        self.age = age    # Instance attribute for age

    # A method to print a greeting
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object (instance) of the class
person1 = Person("Alice", 30)

# Call the greet method on the object
person1.greet()

