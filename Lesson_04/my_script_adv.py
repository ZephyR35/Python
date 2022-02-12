# Доработать скрипт из предыдущего задания:
# теперь он должен работать и из консоли. Используйте аргументы командной строки.


import Utilts
user_input = input('Введите код валюты: ')
user_input_2 = input('Выберите формат вывода. 1 - без даты, 2 - с датой: ')
if user_input_2 == '1':
    print(Utilts.currency_rates(user_input))
elif user_input_2 =='2':
    print(Utilts.currency_rates_advanced(user_input))
else:
    print('Выбран неверный формат')