#todo:
# В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов. Для получения списка всех
# ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword. Приведенный ниже код:
# import keyword
# print(keyword.kwlist)
# выводит: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.
import keyword


def replace_reserve_words(text):
    return ' '.join([i if i not in keyword.kwlist else '<kw>' for i in text.split()])


print(replace_reserve_words('assert in bold english python await function'))
