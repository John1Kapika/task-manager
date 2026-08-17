import json

class Task:
    def __init__(self, task_id, title, done=False):
        self.id = task_id
        self.title = title
        self.done = done

    def mark_done(self):
        # Меняет статус задачи
        self.done = True

    def to_dict(self):
        # Превращает в словарь для JSON
        return {"id": self.id, "title": self.title, "done": self.done}
    @staticmethod
    def from_dict(data):
        # Создаёт задачу из словаря
        return Task(data["id"], data["title"], data["done"])

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load()

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def save(self):
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2, ensure_ascii=False)

    def load(self):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]
            if self.tasks:
                self.next_id = max(task.id for task in self.tasks) + 1
            else:
                self.next_id = 1
        except FileNotFoundError:
            self.tasks = []
            self.next_id = 1
        except json.JSONDecodeError:
            print("Файл tasks.json повреждён. Будет создан новый список задач.")
            self.tasks = []
            self.next_id = 1
    def add(self, title):
        # TODO: создать задачу, добавить, сохранить

        pass

    # TODO: методы delete, mark_done, load, save, get_all