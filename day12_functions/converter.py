def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("1. Convert KM to Miles")
print("2. Convert Celsius to Fahrenheit")
choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    km = float(input("Enter kilometers: "))
    print("Miles:", km_to_miles(km))
elif choice == "2":
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))
else:
    print("Invalid choice")

