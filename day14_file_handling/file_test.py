# Writing to a file
with open("demo.txt", "w") as f:
    f.write("First line\nSecond line")

# Reading the file
with open("demo.txt", "r") as f:
    print("File contents:")
    for line in f:
        print(line.strip())

