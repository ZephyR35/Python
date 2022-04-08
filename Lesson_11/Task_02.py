#Создать собственный класс-исключение, для обработки ситуации деления на ноль и функцию, выполняющую деление двух чисел.


class MyException(ZeroDivisionError): pass


def calc_number(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print(f'Делимое - {a}\n'
              f'Делитель - {b}')
        raise MyException()


try:
    print(calc_number(1,0))
except MyException:
    print(f'Деление на ноль!')

print('--------')

try:
    print(calc_number(1,2))
except MyException:
    print(f'Деление на ноль!')

print('--------')

try:
    print(calc_number(4,2))
except MyException:
    print(f'Деление на ноль!')

