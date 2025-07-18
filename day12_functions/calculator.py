def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("🧮 Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", add(a, b))
elif operation == "-":
    print("Result:", subtract(a, b))
elif operation == "*":
    print("Result:", multiply(a, b))
elif operation == "/":
    print("Result:", divide(a, b))
else:
    print("Invalid operation")

