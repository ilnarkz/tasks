#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT


def get_rnk(dnk):
    chars_dict = {
        'C': 'G',
        'G': 'C',
        'A': 'T',
        'T': 'A'
    }
    result = ''
    for i in dnk:
        result += chars_dict[i]
    return result


print(get_rnk('GGCTAA'))
