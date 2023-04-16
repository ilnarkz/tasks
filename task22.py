#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.
import string


def code(text, n):
    result = ''
    for i in text:
        if i in string.ascii_lowercase:
            char = string.ascii_lowercase.index(i)
            index = (char + n) % (len(string.ascii_lowercase) - 1)
            result += string.ascii_lowercase[index]
        elif i in string.ascii_uppercase:
            char = string.ascii_uppercase.index(i)
            index = (char + n) % (len(string.ascii_uppercase) - 1)
            result += string.ascii_uppercase[index]
        else:
            result += i
    return result
