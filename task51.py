#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ


class Person:
    def __init__(self, last_name, first_name, father_name):
        self.last_name = last_name
        self.first_name = first_name
        self.father_name = father_name

    def __str__(self):
        return self.father_name[::-1] + self.first_name[::-1] + self.last_name[::-1]


p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
