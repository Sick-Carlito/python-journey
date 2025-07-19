filename = "example.txt"  # File to open

try:
    with open(filename, "r") as file:            # Try opening the file in read mode
        content = file.read()                    # Try reading content
        print(content)                           # Print file content
except FileNotFoundError:
    print(f"❌ File '{filename}' not found.")     # Handle file not found error
finally:
    print("📂 File access attempted.")           # Always runs
