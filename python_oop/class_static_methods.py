
class Employee:
    # Class variable shared across all instances
    company_name = "TechStars"

    def __init__(self, name, position):
        self.name = name          # Instance variable: employee's name
        self.position = position  # Instance variable: employee's position

    # Instance method (uses self)
    def introduce(self):
        print(f"Hi, I'm {self.name}, working as a {self.position} at {self.company_name}.")

    # Class method (uses cls)
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name  # Change the company name for all employees

    # Static method (doesn't use self or cls)
    @staticmethod
    def company_policy():
        print("All employees must wear ID badges.")


# Create an employee
emp1 = Employee("Alice", "Engineer")
emp1.introduce()

# Call class method to change company name
Employee.change_company("CodeMasters")

# Create another employee
emp2 = Employee("Bob", "Designer")
emp2.introduce()

# Call static method
Employee.company_policy()

