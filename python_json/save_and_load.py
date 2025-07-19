import json

# 📚 Sample student record
student = {
    "name": "John Doe",
    "class": "Form 4",
    "subjects": ["Math", "English", "Biology"],
    "passed": True
}

# ✅ Save to JSON
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)

# ✅ Load from JSON
with open("student.json", "r") as f:
    loaded_student = json.load(f)

print("📄 Loaded Student Info:")
print(f"Name: {loaded_student['name']}")
print(f"Class: {loaded_student['class']}")

