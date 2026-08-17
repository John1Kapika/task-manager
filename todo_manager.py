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

    def find_task(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        try:
            task_id = int(input("Введите номер задачи: "))
        except ValueError:
            print("Нужно ввести число!")
            return
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return print("Задача не найдена.")

    def add(self, title):
        # TODO: создать задачу, добавить, сохранить

        pass

    # TODO: методы delete, mark_done, load, save, get_all