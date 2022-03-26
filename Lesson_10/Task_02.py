#Реализовать проект расчёта суммарного расхода ткани на производство одежды.

from abc import ABC,abstractmethod

class Clothes(ABC):

    def __init__(self,name):
        self.name = name
    @abstractmethod
    def cloth_cost(self):
        raise NotImplementedError


class Coat(Clothes):
    def __str__(self):
        return f'Имя - {self.name}\n'\
               f'Размер - {self.size}\n'\
               f'Общее количество ткани - {round(self.summary_cloth,3)}'
    summary_cloth = 0

    def __init__(self,size):
        self.size = size
        super().__init__(name = 'Пальто')

    def cloth_cost(self):
        result = (self.size/6.5 * 0.5)
        return result

    def add_to_summary(self):
        self.summary_cloth += self.cloth_cost()

    def show_summary_cloth(self):
        return self.summary_cloth
class Costume(Clothes):
    summary_cloth = 0

    def __str__(self):
        return f'Имя - {self.name}\n'\
               f'Размер - {self.size}\n'\
               f'Общее количество ткани для пошива - {self.summary_cloth}'

    def __init__(self,size):
        self.size = size
        super().__init__(name = 'Костюм')

    def cloth_cost(self):
        result = (self.size*2 + 0.3)
        return result

    def add_to_summary(self):
        self.summary_cloth += self.cloth_cost()

    def show_summary_cloth(self):
        return self.summary_cloth

coat1 = Coat(10)
costume = Costume(10)