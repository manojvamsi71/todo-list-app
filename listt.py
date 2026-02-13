import os

FILE = "tasks.txt"

def show_tasks():
    if not os.path.exists(FILE):
        print("No tasks yet.\n")
        return
    
    with open(FILE, "r") as f:
        tasks = f.readlines()

    if not tasks:
        print("No tasks yet.\n")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")
    print()

def add_task():
    task = input("Enter new task: ")
    with open(FILE, "a") as f:
        f.write(task + "\n")
    print("Task added!\n")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))

    with open(FILE, "r") as f:
        tasks = f.readlines()

    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        with open(FILE, "w") as f:
            f.writelines(tasks)
        print("Task deleted!\n")
    else:
        print("Invalid task number\n")

def main():
    while True:
        print("==== TO-DO LIST ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
