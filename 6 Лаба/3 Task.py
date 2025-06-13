from datetime import datetime

class Task():
    def __init__(self,date_start,date_finish,description):
        self.date_start = datetime.strptime(date_start, "%Y-%m-%d %H:%M:%S")
        self.date_finish = datetime.strptime(date_finish, "%Y-%m-%d %H:%M:%S")
        self.description = description

    
tasks = [
    Task("2023-01-15 09:00:00", "2023-01-15 11:30:00", "Совещание"),
    Task("2023-01-15 13:00:00", "2023-01-15 18:00:00", "Разработка функционала"),
    Task("2023-01-16 10:00:00", "2023-01-16 15:00:00", "Обед"),
    Task("2023-01-17 14:00:00", "2023-01-17 19:00:00", "Тестирование"),
    Task("2023-01-17 18:00:00", "2023-01-17 19:30:00", "Вывод результатов")
]

last_task = tasks[0]
for task in tasks:
    if task.date_finish > last_task.date_finish:
        last_task = task

print(f"Начало занятия: {last_task.date_start} конец занятия: {last_task.date_finish} описание: {last_task.description}")
