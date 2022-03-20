# Реализуйте класс Car (машина).
# Техническое задание:
#
# атрибуты: speed, color, name, is_police(булево). speed - текущая скорость машины.
# методы: go, stop, turn(direction), которые должны сообщать(выводить на экран), что машина поехала,
# остановилась, повернула (куда). turn(direction) - метод, принимающий параметр: направление поворота.
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

from random import choice

class Car():
    horse_force = 735.49875 / 16
    colors = ['White','Blue','Green','Black']
    def __init__(self,power_eng,name='car',is_police = False):
        self.speed = 0
        self.mass = 1500
        self.color = choice(self.colors)
        self.name = name
        self.is_police = is_police
        self.power_eng = power_eng * self.horse_force
        self.tire_friction = 2
        self.gas_acc = self.power_eng / self.mass
        self.break_acc = -9.81 / self.tire_friction

    def show_info(self):
        print(f'Цвет машины:{self.color}')
        print(f'Масса автомобиля:{self.mass}')
        print(f'Имя автомобиля:{self.name}')
        if self.is_police == True:
            print('Ваш автомобиль из полиции')
        print(f'Мощность двигателя:{self.power_eng}')

    def go(self,duration):
        self.speed = self.speed + (duration*self.gas_acc)
        print(f'Вы разгонялись {duration} секунд')

    def stop(self,duration):
        self.speed = self.speed + (duration * self.break_acc)
        if self.speed<=0:
            print('Вы остановились')
            self.speed = 0


        print(f'Вы тормозили {duration} секунд')


    def turn(self,direction):
        if direction == 'left':
            print('Вы повернули налево')
        if direction == 'right':
            print('Вы повернули направо')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self,power_eng,name='Towncar',is_police = False):
        super().__init__(power_eng,name='Towncar')
        self.mass = 1200

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость!')
            print(f'Ваша скорость:{self.speed},ограничение:{60}')
        else:
            print(self.speed)
class WorkCar(Car):
    def __init__(self,power_eng,name='Workcar',is_police = False):
        super().__init__(power_eng,name='Workcar')
        self.mass = 4000

    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость!')
            print(f'Ваша скорость:{self.speed},ограничение:{40}')
        else:
            print(self.speed)

class SportCar(Car):
    def __init__(self,power_eng,name='Sportcar',is_police = False):
        super().__init__(power_eng,name='Sportcar')
        self.mass = 1300

class PoliceCar(Car):
    def __init__(self,power_eng,name='PoliceCar',is_police = True):
        super().__init__(power_eng,name='PoliceCar',is_police=True)
        self.mass = 2000
        self.color = 'Black'
    def lights_on(self,switch):
        if switch == 1:
            print('Вы включили проблесковый маяк')
        if switch == 0:
            print('Вы выключили проблесковый маяк')

c1 = Car(140)
t1 = TownCar(120)
w1 = WorkCar(130)
s1 = SportCar(250)
p1 = PoliceCar(145)