#Реализовать класс «Дата».
class DateInitError(ValueError):
    pass


class Date():
    def __init__(self, date):
        try:
            date = self.date_search(date)
            date = self.date_validation(date)
        except ValueError:
            raise DateInitError("Неверно задан формат даты!")
        else:
            self.date = date

    @classmethod
    def date_search(cls,date):
        splited_date = date.split('-')
        day,month,year = splited_date
        result = [int(day),int(month),int(year)]
        if len(result) != 3:
            raise ValueError
        return result

    @staticmethod
    def date_validation(date):
        day,month,year = date
        if 1<=day<=31 and 1<=month<=12 and 0<=year<=2022:
            return day,month,year
        else:
            raise ValueError



    def __str__(self):
        return f'{self.date[2]}.{self.date[1]}.{self.date[0]}'

date_1 = '25-12-2015'
date_2 = '22-04-2002'
date_3 = '32-13-2015'
date_4 = '8-09--2019'

date_lst = [date_1,date_2,date_3,date_4]
for i in date_lst:
    try:
        print(Date(i))
    except DateInitError:
        print('Неверно задан формат даты!')