# Day 3 - User Input & Type Conversion

# Ask the user's name and age
name = input("What's your name? ")
age = int(input("How old are you? "))

# Greet the user
print("Hi", name + "!", "You are", age, "years old.")

# Future age calculator
future_years = 5
future_age = age + future_years
print("In", future_years, "years, you'll be", future_age)

# Ask for 2 numbers and add them
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total = num1 + num2
print("The total is:", total)


