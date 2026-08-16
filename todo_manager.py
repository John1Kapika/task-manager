import json
numberTask = None
nextID = int(0)
listTask = []

def main():
    global listTask, nextID
    listTask = load_tasks()
    # Восстанавливаем счётчик
    if listTask:
        max_id = max(task['id'] for task in listTask)
        nextID = max_id
    else:
        nextID = 0
    print(f"Загружено {len(listTask)} задач.")
    while True:
        try:
            numberTask = int(input(
                  "------------------------------\n1. Добавить задачу\n2. Показать все задачи\n3. Отметить задачу выполненной\n4. Удалить задачу"
                  "\n5. Выход\n\nНапишите номер действия: "))
            print("------------------------------")
        except ValueError:
            print("Пожалуйста, введите число.")
            continue
        if numberTask == 1:
            new_task()
        elif numberTask == 2:
            all_task()
        elif numberTask == 3:
            yes_task()
        elif numberTask == 4:
            delete_task()
        elif numberTask == 5:
            exit()
            break
        else:
            print("Неверный номер\n")

def new_task():
    global nextID, listTask
    nextID = int(nextID + 1)
    task = {'id': nextID, 'title': input("Опишите новую задачу: "), 'done': False}
    listTask.append(task)
    save_tasks(listTask)
    print("Задача успешно добавлена.")

def all_task():
    if not listTask:
        print("Список задач пуст.")
        return
    for idx, task in enumerate(listTask, start=1):
        if task['done'] == False:
            print(task['id'], ". [ ] ", task['title'], sep='')
        else:
            print(task['id'], ". [X] ", task['title'], sep='')

def yes_task():
    global listTask
    if not listTask:
        print("Список задач пуст.")
        return
    try:
        task_id = int(input("Введите номер выполненной задачи: "))
    except ValueError:
        print("Нужно ввести число.")
        return
    for task in listTask:
        if task['id'] == task_id:
            if task['done']:
                print("Уже выполнена.")
            else:
                task['done'] = True
                save_tasks(listTask)
                print("Выполнена!")
            return
    print("Задача не найдена.")

def delete_task():
    global listTask
    if not listTask:
        print("Список задач пуст.")
        return
    try:
        task_id = int(input("Введите номер задачи, помечаемой на удаление: "))
    except ValueError:
        print("Нужно ввести число.")
        return
    for task in listTask:
        if task['id'] == task_id:
            listTask.remove(task)
            save_tasks(listTask)
            print("Задача удалена.")
            return
    print("Задача не найдена.")

def exit():
    print("С Вами было приятно иметь дело.\nУспешного завершения дел!")

def load_tasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # если файла нет — пустой список
    except json.JSONDecodeError:
        # Файл есть, но содержит невалидный JSON — возвращаем пустой список
        # (можно также вывести предупреждение или переименовать старый файл)
        print("Файл tasks.json повреждён. Будет создан новый список задач.")
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)