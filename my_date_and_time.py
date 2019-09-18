from datetime import datetime, date, timedelta
import datedelta
"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
def split_myday(day):
    #day_split = str(day).split()
    
    #yesterday_final = day.date()
    yesterday_parse = day.strftime('%d.%m.%Y')
    return yesterday_parse


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.now()
    
    delta = timedelta(days=1)
    yesterday = today - delta

    delta_month = datedelta.datedelta(months = 1)
    last_month = today - delta_month
    
    print(split_myday(yesterday))
    print(split_myday(today))
    print(split_myday(last_month))

def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #string_final = string[:-7]
    date_dt = datetime.strptime(string, '%m/%d/%y %H:%M:%S.%f')
    return date_dt, type(date_dt)

if __name__ == "__main__":
    print_days()
    d, t = str_2_datetime("01/01/17 12:10:03.234567")
    print(d,t)