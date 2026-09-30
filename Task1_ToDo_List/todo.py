# CodSoft Internship - Task 1
# To-Do List Application

tasks = []


def add_task():
    task = input("\nEnter task: ").strip()

    if task:
        tasks.append(task)
        print("\nTask added successfully!")
    else:
        print("\nTask cannot be empty.")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== MY TASKS ==========")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("==============================")


def update_task():
    if not tasks:
        print("\nNo tasks available to update.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to update: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter new task: ").strip()

            if new_task:
                tasks[task_number - 1] = new_task
                print("\nTask updated successfully!")
            else:
                print("\nTask cannot be empty.")
        else:
            print("\nInvalid task number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def delete_task():
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"\nTask deleted successfully: {deleted_task}")
        else:
            print("\nInvalid task number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def main():
    while True:
        print("\n================================")
        print("       TO-DO LIST APPLICATION")
        print("================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("\nThank you for using To-Do List Application!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()