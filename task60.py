# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!


def is_goor_password(passwords):
    for password in passwords:
        digits = []
        letters = []
        if len(password) < 9:
            print('LengthError')
            continue
        for char in password:
            if char.isdigit():
                digits.append(char)
            elif char.isalpha():
                letters.append(char)
            else:
                continue
        if ''.join(letters) == ''.join(letters).lower():
            print('LetterError')
            continue
        if not digits:
            print('DigitError')
            continue
        if len(password) >= 9 and digits and ''.join(letters) != ''.join(letters).lower():
            return 'Success'


print(is_goor_password(['arr1', 'Arrrrrrrrrrr', 'arrrrrrrrrrrrrrr1', 'Arrrrrrr1']))
print('-' * 20)
print(is_goor_password(['beegeek', 'Beegeek123', 'Beegeek2022', 'Beegeek2023', 'Beegeek2024']))

