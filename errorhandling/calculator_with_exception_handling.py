
# 📟 A simple calculator that handles errors gracefully

def calculate():
    try:
        x = float(input("Enter first number: "))       # Get first number
        op = input("Enter operator (+, -, *, /): ")    # Get operator
        y = float(input("Enter second number: "))      # Get second number

        if op == '+':
            print(f"Result: {x + y}")
        elif op == '-':
            print(f"Result: {x - y}")
        elif op == '*':
            print(f"Result: {x * y}")
        elif op == '/':
            if y == 0:
                raise ZeroDivisionError("❌ Cannot divide by zero!")  # Custom error
            print(f"Result: {x / y}")
        else:
            raise ValueError("❌ Invalid operator!")  # Custom error
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math Error: {zde}")
    finally:
        print("🧮 Calculation completed.")

calculate()
