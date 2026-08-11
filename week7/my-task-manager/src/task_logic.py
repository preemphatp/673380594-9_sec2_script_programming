def get_next_task_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

def add_task(tasks, description):
    task_id = get_next_task_id(tasks)
    tasks.append({"id": task_id, "description": description, "completed": False})
    print(f"Task '{description}' added with ID {task_id}.")
    return tasks

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "Completed" if task['completed'] else "Pending"
        print(f"ID: {task['id']} | Description: {task['description']} | Status: {status}")
    print("------------------")

def complete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task ID {task_id} marked as completed.")
            return tasks
    print(f"Error: Task with ID {task_id} not found.")
    return tasks

def delete_task(tasks, task_id):
    original_len = len(tasks)
    tasks[:] = [t for t in tasks if t['id'] != task_id]
    if len(tasks) < original_len:
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")
    return tasks