import csv

# Create a list of student records including the header
students = [
    ["student_id", "name", "grade"],  # Header row
    [101, "John", "B"],
    [102, "Maya", "A"],
    [103, "Leo", "C"],
    [104, "Eva", "A"],
    [105, "Nina", "B"]
]

# Create and write to the CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("✅ students.csv created successfully.")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        student_id, name, grade = row
        print(f"Student {name} (ID: {student_id}) scored grade {grade}")
