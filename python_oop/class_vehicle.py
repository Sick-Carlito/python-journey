# Define the parent class Vehicle
class Vehicle:
    # Class variable shared by all Vehicle instances
    wheels = 4

    # Constructor: runs when a new Vehicle object is created
    def __init__(self, brand, model):
        self.brand = brand    # Instance variable: brand of the vehicle
        self.model = model    # Instance variable: model of the vehicle

    # Instance method: works on specific objects
    def display_info(self):
        print(f"{self.brand} {self.model} has {self.wheels} wheels.")

    # Class method: modifies the class variable (for all objects)
    @classmethod
    def change_wheels(cls, number):
        cls.wheels = number
        print(f"Number of wheels changed to {cls.wheels} for all Vehicles.")

    # Static method: independent of class or object
    @staticmethod
    def safety_tip():
        print("Safety Tip: Always wear a seatbelt while driving.")

# Subclass of Vehicle
class Bike(Vehicle):
    wheels = 2  # Override the class variable for bikes

    # You can override display_info() if needed, but it's inherited and still works

# Create an instance of Bike
bike = Bike("Yamaha", "MT-15")
bike.display_info()  # Should print 2 wheels

# Bike still has access to Vehicle's methods
bike.safety_tip()  # Inherited static method

# Changing Vehicle wheels does NOT affect bikes
Vehicle.change_wheels(8)
bike.display_info()  # Still 2 wheels




# Create an instance of Vehicle
car = Vehicle("Toyota", "Corolla")
car.display_info()  # Should print 4 wheels

# Call the static method
Vehicle.safety_tip()

# Change wheels for all Vehicle objects
Vehicle.change_wheels(6)

# Display info again
car.display_info()  # Should now show 6 wheels
