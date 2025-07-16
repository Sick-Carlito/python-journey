# Day 6 - Working with Lists

# Create a list
fruits = ["apple", "banana", "orange"]

# Print each fruit
print("Original list:")
for fruit in fruits:
    print(fruit)

# Add new fruits
fruits.append("mango")
fruits.insert(1, "kiwi")

# Remove an item
fruits.remove("banana")

# Replace an item
fruits[0] = "grapes"

# Final list
print("\nUpdated list:")
for fruit in fruits:
    print(fruit)

# Count
print("\nTotal fruits:", len(fruits))

