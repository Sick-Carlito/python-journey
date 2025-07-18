def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    print("\nYour Notes:")
    with open("notes.txt", "r") as file:
        for line in file:
            print("- " + line.strip())

print("1. Write a new note")
print("2. View saved notes")

choice = input("Choose an option: ")

if choice == "1":
    note = input("Enter your note: ")
    save_note(note)
elif choice == "2":
    view_notes()
else:
    print("Invalid choice.")

