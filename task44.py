#todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами. Накапливает сон обеих функций отдельно и печатает две суммы.
import time


def sleep_two_seconds():
    time.sleep(2)
    print('Функция проспала 2 секунды')


def sleep_three_seconds():
    time.sleep(3)
    print('Функция проспала 3 секунды')


def main():
    sum_func_1 = 0
    sum_func_2 = 0
    for i in range(10):
        if i % 2 == 0:
            print(i)
            sleep_two_seconds()
            sum_func_1 += 2
        else:
            print(i)
            sleep_three_seconds()
            sum_func_2 += 3
    print(f'Сумма сна первой функции = {sum_func_1}')
    print(f'Сумма сна второй функции = {sum_func_2}')


print(main())
