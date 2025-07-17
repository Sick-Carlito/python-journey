# Day 11 - Simple To-Do Checklist App

tasks = []

print("📝 To-Do List App (type 'done' to finish adding tasks)")

while True:
    task = input("Enter task: ")
    if task.lower() == "done":
        break
    tasks.append(task)

print("\n✅ Your To-Do List:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

