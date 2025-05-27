from datetime import datetime

def date_conversion(date_input):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    months = [
        "Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
        "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"
    ]
    
    date = datetime.strptime(date_input, "%d.%m.%Y")
    
    weekday_name = days[date.weekday()]
    month_name = months[date.month - 1]  
    
    return f"{weekday_name}, {date.day} {month_name}, {date.year} год"


date_input = input("Введите дату (формат ДД.ММ.ГГГГ): ")


print(date_conversion(date_input))