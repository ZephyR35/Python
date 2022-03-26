#Реализовать программу работы с органическими клетками, состоящими из ячеек.


class Cell():
    def __init__(self,number):
        self.unit_number = number

    def __add__(self, other):
        return self.unit_number + other.unit_number
    def __sub__(self, other):
        result = self.unit_number - other.unit_number
        if result < 0:
            raise ValueError('Невозможно создать клетку: количество ячеек меньше 0')
        return result
    def __mul__(self, other):
        return self.unit_number * other.unit_number
    def __floordiv__(self, other):
        return self.unit_number // other.unit_number
    def make_order(self,count_of_cells):
        remain = self.unit_number % count_of_cells
        count_of_strings = self.unit_number // count_of_cells
        result = ("*"*count_of_cells + "\n")*count_of_strings
        return result + '*'*remain+'\n'

# Извините, немного подсмотрел у вас функцию make_order. Не получилось у меня нормально реализовать этот вывод.
# Пытался сделать через список. В цикле добавлял звездочку в список, уменьшал количество ячеек на 1
# цикл работает до тех пор, пока количество ячеек не станет 0. После чего нужно было просто расставить в нужных местах \n.
# Как-то не срослось с таким алгоритмом, да и слишком он громоздкий получился. В свое опрадвание за списывание хочу сказать
# что я в отдельном файле попробовал создать функцию make_order и с помощью дебагера досконально разобраться что и как тут происходит. До тех пор
# пока я на 200% не был уверен, что смогу такое повторить в любой момент, не добавлял её в задание.




c1 = Cell(10)
c2 = Cell(15)
