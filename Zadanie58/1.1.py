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

class ZateExt(Zate):
    def add_years(self, years):
        self.date = self.date.replace(year=self.date.year + years)

    def subtract_years(self, years):
        self.date = self.date.replace(year=self.date.year - years)

    def add_months(self, months):
        year = (self.date.year + (self.date.month - 1 + months) // 12)
        month = ((self.date.month - 1 + months) % 12) + 1
        self.date = self.date.replace(year=year, month=month)

    def subtract_months(self, months):
        year = (self.date.year - 1) + ((self.date.month - 1 - months) // 12)
        month = ((self.date.month - 1 - months) % 12) + 1
        self.date = self.date.replace(year=year, month=month)

    def add_days(self, days):
        self.date += datetime.timedelta(days=days)

    def subtract_days(self, days):
        self.date -= datetime.timedelta(days=days)


z = ZateExt(2023, 10, 29)
print(z.get_year())
print(z.get_month_number())
print(z.get_day_of_month())

z.add_years(5)
print(z.get_year())

z.subtract_months(3)
print(z.get_month_number())

z.add_days(15)
print(z.get_day_of_month())