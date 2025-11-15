import argparse
from command import add_task, list_tasks, remove_task  # استيراد الدوال

def main():
    parser = argparse.ArgumentParser(description="To Do Application")
    parser.add_argument('--action', '--act', type=str, choices=['add', 'list', 'remove'], required=True,
                        help="Action to perform (add, list, remove)")
    parser.add_argument('--task', '--t', type=str, help="Task description")
    parser.add_argument('--time', '--ti', type=str, help="Time for the task (HH:MM format if adding)")
    args = parser.parse_args()

    if args.action == 'add':
        if not args.task or not args.time:
            print("Error: --task and --time are required for adding a task.")
            return
        add_task(args.task, args.time)

    elif args.action == 'list':
        list_tasks()

    elif args.action == 'remove':
        if not args.task:
            print("Error: --task is required for removing a task.")
            return
        remove_task(args.task)


if __name__ == "__main__":
    main()
