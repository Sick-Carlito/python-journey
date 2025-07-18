import conversions

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", conversions.c_to_f(c))
elif choice == "2":
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", conversions.f_to_c(f))
else:
    print("Invalid choice")

