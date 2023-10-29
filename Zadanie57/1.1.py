import datetime

class Zate:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month_number(self):
        return self.date.month

    def get_day_of_month(self):
        return self.date.day

    def get_weekday_number(self):
        return self.date.weekday()

    def get_weekday_name(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return days[self.date.weekday()]

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.date.month - 1]


z = Zate(2023, 10, 29)
print(z.get_year())
print(z.get_month_number())
print(z.get_day_of_month())
print(z.get_weekday_number())
print(z.get_weekday_name())
print(z.get_month_name())