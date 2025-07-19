# Day 9 - Gym Access Checker

age = int(input("How old are you? "))
has_membership = input("Do you have a membership? (yes/no): ").lower() == "yes"
has_pass = input("Do you have a day pass? (yes/no): ").lower() == "yes"

if (has_membership or has_pass) and age >= 16:
    print("✅ You may enter the gym.")
else:
    print("❌ Access denied.")


# Not Logic

is_banned = input("Are you banned from commenting? (yes/no): ").lower() == "yes"

if not is_banned:
    print("✅ You can post your comment.")
else:
    print("❌ You're banned from commenting.")


