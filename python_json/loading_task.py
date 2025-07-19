import json  # Step 1: Import the built-in JSON module

# Step 2: Create a Python dictionary representing an employee
employee = {
    "id": 101,
    "name": "James",
    "role": "Data Analyst",
    "skills": ["SQL", "Excel", "Python"],
    "remote": True
}

# Step 3: Save the employee data to a JSON file
with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)  
    # json.dump() writes the Python dictionary to a JSON file
    # indent=4 makes it nicely formatted (pretty printed)

# Step 4: Load the data back from the JSON file into a new variable
with open("employee.json", "r") as file:
    loaded_employee = json.load(file)  
    # json.load() reads and converts the JSON back into a Python dict

# Step 5: Print the loaded data in a readable sentence
# We use the loaded_employee dictionary to extract the values
name = loaded_employee["name"]
role = loaded_employee["role"]
skills = ", ".join(loaded_employee["skills"])  # Turn skills list into comma-separated string

# Step 6: Construct the final sentence and print it
print(f"{name} works as a {role} and knows {skills}.")
# Expected output: James works as a Data Analyst and knows SQL, Excel, Python.

