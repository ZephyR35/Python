#Реализовать класс Matrix (матрица).

#Сделал класс для матриц 3х3. Понимаю, что для реализации других шаблонов матриц можно использовать *args
# и через распаковку списка *args создавать любые матрицы, но решил остановиться на конкретном примере 3х3.

a_1 = [1,2,3]
b_1 = [45,12,23]
c_1 = [65,23,47]

a_2 = [11,22,33]
b_2 = [21,56,47]
c_2 = [55,90,89]

class Matrix():

    def __init__(self,lst_1,lst_2,lst_3):
        self.lst_1 = lst_1
        self.lst_2 = lst_2
        self.lst_3 = lst_3

    def __str__(self):
        if len(self.lst_1) < 3 or len(self.lst_2) < 3 or len(self.lst_3) < 3:
            raise ValueError('Неверная длина списков!')
        return f'|{self.lst_1[0]} {self.lst_1[1]} {self.lst_1[2]}|\n'\
               f'|{self.lst_2[0]} {self.lst_2[1]} {self.lst_2[2]}|\n'\
               f'|{self.lst_3[0]} {self.lst_3[1]} {self.lst_3[2]}|'
    def __add__(self, other):
        if len(self.lst_1) < 3 or len(self.lst_2) < 3 or len(self.lst_3) < 3:
            raise ValueError('Неверная длина списков!')
        if len(other.lst_1) < 3 or len(other.lst_2) < 3 or len(other.lst_3) < 3:
            raise ValueError('Неверная длина списков!')
        return f'|{self.lst_1[0] + other.lst_1[0]} {self.lst_1[1] + other.lst_1[1]} {self.lst_1[2] + other.lst_1[2]}|\n'\
               f'|{self.lst_2[0] + other.lst_2[0]} {self.lst_2[1] + other.lst_2[1]} {self.lst_2[2] + other.lst_2[2]}|\n'\
               f'|{self.lst_3[0] + other.lst_3[0]} {self.lst_3[1] + other.lst_3[1]} {self.lst_3[2] + other.lst_3[2]}|'

m1 = Matrix(a_1,b_1,c_1)
m2 = Matrix(a_2,b_2,c_2)
