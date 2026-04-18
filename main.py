import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    return "Tasks saved successfully!"


def add_task(tasks):
    task = input("Enter a task: ").strip()
    if not task:
        return "Task cannot be empty!"

    tasks.append(task)
    return f'"{task}" added.'


def view_tasks(tasks):
    if not tasks:
        return "No tasks available."

    output = ""
    for i, task in enumerate(tasks, 1):
        output += f"{i}. {task}\n"

    return output.strip()


def delete_task(tasks):
    if not tasks:
        return "No tasks available."

    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            return f'"{removed}" deleted successfully'
        else:
            return "Invalid task number!"
    except ValueError:
        return "Enter a valid number!"


def main():
    tasks = load_tasks()

    while True:
        try:
            print("\n1. Add Task")
            print("2. View Tasks")
            print("3. Delete")
            print("4. Save Tasks")
            print("5. Exit")

            choice = int(input("Choose (1-5): "))

            if choice == 1:
                print(add_task(tasks))
            elif choice == 2:
                print(view_tasks(tasks))
            elif choice == 3:
                print(delete_task(tasks))
            elif choice == 4:
                print(save_tasks(tasks))
            elif choice == 5:
                save_tasks(tasks)
                print("Tasks saved. Bye 👋")
                break
            else:
                print("Choose 1, 2, 3, 4, or 5")
        except ValueError:
            print("Please enter a valid whole number!")


if __name__ == "__main__":
    main()



