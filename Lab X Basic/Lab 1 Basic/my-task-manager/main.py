import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import task_data
import task_logic

def display_menu():
    print("\n--- Task Manager Menu ---\n1. Add Task\n2. List Tasks\n3. Complete Task\n4. Delete Task\n5. Exit\n-------------------------")

def main():
    tasks = task_data.load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            desc = input("Enter task description: ").strip()
            if desc: tasks = task_logic.add_task(tasks, desc)
        elif choice == '2':
            task_logic.list_tasks(tasks)
        elif choice == '3':
            try: tasks = task_logic.complete_task(tasks, int(input("Enter Task ID: ")))
            except ValueError: print("Invalid input. Enter a number.")
        elif choice == '4':
            try: tasks = task_logic.delete_task(tasks, int(input("Enter Task ID: ")))
            except ValueError: print("Invalid input. Enter a number.")
        elif choice == '5':
            task_data.save_tasks(tasks)
            print("Saving tasks and exiting. Goodbye!")
            break

if __name__ == "__main__":
    main()