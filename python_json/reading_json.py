import json

# 📁 Read data from a JSON file
with open("user.json", "r") as file:
    data = json.load(file)  # Convert JSON to Python dictionary

print(data)  # Output the Python dict
print(data["name"])  # Access data like a dictionary
