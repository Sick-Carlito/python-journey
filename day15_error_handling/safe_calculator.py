try:
    num1 = float(input("Enter first number: "))
    op = input("Choose operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid operator.")
except ValueError:
    print("Please enter numeric values.")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Calculation complete.")

