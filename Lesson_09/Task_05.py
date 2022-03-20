#Реализовать класс Stationery (канцелярская принадлежность).
# Техническое задание:
#
# атрибут title (название)
# метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# Подумайте о том, имеет ли смысл при переопределении draw использовать draw базового класса.
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.



class Stationery():
    def __init__(self):
        self.title = 'Принадлежность'

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        self.title = 'Ручка'
    def draw(self):
        print('Отрисовка ручкой')

class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'
    def draw(self):
        print('Отрисовка карандашом')

class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'
    def draw(self):
        print('Отрисовка маркером')


s1 = Stationery()
pen = Pen()
p1 = Pencil()
h1 = Handle()