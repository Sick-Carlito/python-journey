import json

# 📝 Data to be written
user = {
    "name": "Alice",
    "age": 30,
    "is_active": True,
    "skills": ["Python", "React"]
}

# 📁 Write to a file
with open("output.json", "w") as file:
    json.dump(user, file, indent=4)  # Write nicely formatted JSON

