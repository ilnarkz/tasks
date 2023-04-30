#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def create_strings_list(func):
    def wrapper(*args):
        lst = [i.upper() for i in args if isinstance(i, str)]
        func(args)
        return lst
    return wrapper
@create_strings_list
def get_nothing(*args):
    pass

print(get_nothing(123, 'asd', 'True', True, ['rty', 'zxc'], '_', '123', 'Qaz'))
