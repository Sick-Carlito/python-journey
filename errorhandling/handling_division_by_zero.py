
# Ask the user for two numbers and divide them
try:
    num1 = int(input("Enter numerator: "))       # Convert input to integer
    num2 = int(input("Enter denominator: "))     # Convert input to integer
    result = num1 / num2                          # May raise ZeroDivisionError
    print(f"Result is: {result}")                # Show result if no error
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")            # Handle divide-by-zero error
except ValueError:
    print("❌ Please enter valid numbers!")       # Handle non-integer input
else:
    print("✅ Division completed successfully.")  # Runs if no error happens
finally:
    print("🧾 Operation done.")                   # Always runs
