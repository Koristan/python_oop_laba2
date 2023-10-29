import datetime

class Month:
    def __init__(self, month_number):
        if 1 <= month_number <= 12:
            self.month_number = month_number
        else:
            raise ValueError("Номер месяца должен быть от 1 до 12")

    def get_month_number(self):
        return self.month_number

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.month_number - 1]

    def get_last_day_of_month(self):
        if self.month_number == 12:
            next_month = 1
            next_year = datetime.date.today().year + 1
        else:
            next_month = self.month_number + 1
            next_year = datetime.date.today().year

        last_day_of_month = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
        return last_day_of_month.day

    def get_first_weekday(self):
        first_day = datetime.date(datetime.date.today().year, self.month_number, 1)
        return first_day.weekday()

    def get_last_weekday(self):
        last_day = datetime.date(datetime.date.today().year, self.month_number, self.get_last_day_of_month())
        return last_day.weekday()

m = Month(10)
print(m.get_month_number())
print(m.get_month_name())
print(m.get_last_day_of_month())
print(m.get_first_weekday())
print(m.get_last_weekday())