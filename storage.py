import json , os
file = 'task.json'
def save_task(task):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(task, f, ensure_ascii=False, indent=2)

def load_task():
    if not os.path.exists(file):
        return []
    with open(file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
