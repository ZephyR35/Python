#Создайте собственный класс-исключение, используемый для проверки содержимого списка на наличие только чисел.

def input_valid(inp):
    try:
        int(inp)
        lst.append(int(inp))
    except ValueError:
        raise MyException


class MyException(ValueError):pass



lst = []
user_input = input('Введите целое число для записи в список\n'
                   'Для завершения введите <stop>\n'
                   'Для вывода списка введите <show_list>')
lst.append(int(user_input))
while user_input != 'stop':
    user_input = input('Продолжайте вводить числа')
    if user_input == 'stop':
        print('Программа завершена!')
        print(lst)
        break
    elif user_input == 'show_list':
        print(lst)
        continue
    try:
        input_valid(user_input)
    except MyException:
        print('Вы ввели не число, попробуйте снова')