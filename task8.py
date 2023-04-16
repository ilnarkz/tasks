# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

num = 2332
num_to_str = str(num)
reverse_num = num_to_str[::-1]
print(num_to_str == reverse_num)
