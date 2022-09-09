import datetime as dt


class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        if date == '':
            date_format = dt.datetime.strptime(date, '%d.%m.%Y')
            self.date = date_format
        else:
            self.date = date


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, limit):
        self.limit = limit
        print()

    def get_today_stats(self, limit, date):
        self.limit = limit
        super(Record, self).__init__(date)


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        print()


class CashCalculator(Calculator):
    def __init__(self, EURO_RATE, USD_RATE, limit):
        super().__init__(limit)
        self.USD_RATE = USD_RATE
        self.EURO_RATE = EURO_RATE



# # создадим калькулятор денег с дневным лимитом 1000
# calories_calculator = CaloriesCalculator(1000)

# # дата в параметрах не указана,
# # так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
# cash_calculator.add_record(Record(amount=145, comment="кофе"))
# # и к этой записи тоже дата должна добавиться автоматически
# cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# # а тут пользователь указал дату, сохраняем её
# cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
#
# print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб
