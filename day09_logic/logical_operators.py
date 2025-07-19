# Day 9 - Logical Operators

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

if age >= 18 and has_id:
    print("✅ You are allowed in.")
elif age >= 18 and not has_id:
    print("❌ You need an ID to enter.")
else:
    print("❌ You are underage and cannot enter.")
