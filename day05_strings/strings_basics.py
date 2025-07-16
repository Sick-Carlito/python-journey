# Day 5 - Strings and Text Manipulation

name = input("What is your full name? ")

print("\n--- Text Styling ---")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("Replace spaces with dashes:", name.replace(" ", "-"))

# Count and check
print("Length of name:", len(name))
print("Does it contain 'bond'?", "bond" in name.lower())

# Custom sentence using f-string
age = int(input("\nHow old are you? "))
print(f"Hello, {name.title()}! You're {age} years old. Next year, you'll be {age + 1}.")

