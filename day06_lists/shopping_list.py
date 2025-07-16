# Day 6 - Shopping List App

shopping_list = []

while True:
    item = input("Add an item (or type 'done' to finish): ")

    if item.lower() == "done":
        break
    elif item in shopping_list:
        print(f"{item} is already in your list.")
    else:
        shopping_list.append(item)
        print(f"{item} added.")

print("\nYour final shopping list:")
for item in shopping_list:
    print("-", item)

