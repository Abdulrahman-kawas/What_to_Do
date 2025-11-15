from storage import load_task, save_task
from datetime import datetime

def add_task(task_name, task_time):
    tasks = load_task()
    new_task = {
        'name': task_name,
        'time': task_time,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(new_task)
    save_task(tasks)
    print(f"Task '{task_name}' added with time '{task_time}'.")

def list_tasks():
    tasks = load_task()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['name']} - Time: {task['time']} - Created At: {task['created_at']}")

def remove_task(task_name):
    tasks = load_task()
    updated_tasks = [task for task in tasks if task['name'] != task_name]
    if len(tasks) == len(updated_tasks):
        print(f"No task found with name '{task_name}'.")
    else:
        save_task(updated_tasks)
        print(f"Task '{task_name}' removed.")
