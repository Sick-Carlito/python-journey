# Define the Car class
class Car:
    # The constructor (__init__) runs when we create a new Car object
    def __init__(self, brand, model, year):
        self.brand = brand    # Set the car's brand (e.g., Toyota)
        self.model = model    # Set the car's model (e.g., Corolla)
        self.year = year      # Set the car's year (e.g., 2020)

    # Define a method to display information about the car
    def display_info(self):
        # This method prints the car's details using the object's attributes
        print(f"This car is a {self.brand} {self.model} from {self.year}.")

# Create a Car object by providing brand, model, and year
my_car = Car("Toyota", "Corolla", 2020)

# Call the display_info() method to print car details
my_car.display_info()

