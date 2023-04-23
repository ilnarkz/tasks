# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.
from calendar import monthrange


def get_dates(year, month):
    days_in_month = monthrange(year, month)[1]
    return [f'{i}-{month}-{year}' for i in range(1, days_in_month + 1)]


print(get_dates(2023, 4))
