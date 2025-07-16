# Day 8 - Voting Eligibility Checker

age = int(input("Enter your age: "))

if age >= 18:
    print("✅ You are eligible to vote.")
    years_until_100 = 100 - age
    print(f"You'll be 100 in {years_until_100} years!")
elif age > 0:
    print("❌ You're not old enough to vote.")
    print(f"Please come back in {18 - age} years.")
else:
    print("Please enter a valid age.")


# Grading System


score = int(input("Enter your score (0–100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F. You need improvement.")

