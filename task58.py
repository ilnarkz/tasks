#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.
from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, velocity, cost, price):
        self.velocity = velocity
        self.cost_ = cost
        self.price = price

    @abstractmethod
    def cost(self):
        return self.price

    @abstractmethod
    def info(self):
        return f'Velocity = {self.velocity}, cost = {self.cost_}, price = {self.price}'


class Marine(Transport):
    def cost(self):
        return self.price

    def info(self):
        return f'Velocity = {self.velocity}, cost = {self.cost_}, price = {self.price}'


class Ground(Transport):
    def cost(self):
        return self.price

    def info(self):
        return f'Velocity = {self.velocity}, cost = {self.cost_}, price = {self.price}'


# t = Transport(22, 100, 200)
# print(t)
g = Ground(80, 50, 100)
print(g.info())
print(g.cost())

m = Marine(20, 100, 200)
print(m.info())
print(m.cost())
