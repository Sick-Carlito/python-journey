# Day 4 - Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Choose operator (+, -, *, /, %, **): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
elif operator == "%":
    print("Result:", num1 % num2)
elif operator == "**":
    print("Result:", num1 ** num2)
else:
    print("Invalid operator")

