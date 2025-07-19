# Ask user for a note to save
note = input("Write a note to save: ")

# Save the note to a file
with open("my_notes.txt", "a") as file:
    file.write(note + "\n")  # Save each note on a new line

# Load and display all notes
print("\nYour saved notes:")
with open("my_notes.txt", "r") as file:
    for line in file:
        print("- " + line.strip())

