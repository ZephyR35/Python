# Написать свой модуль utils и перенести в него функцию currency_rates и currency_rates_advanced
# Создать скрипт, импортировать в него модуль utils и выполнить несколько вызовов функции currency_rates.
# Убедиться, что ничего лишнего не происходит.


import Utilts
print(Utilts.currency_rates('USd'))
print(Utilts.currency_rates('KZT'))
print(Utilts.currency_rates('EUR'))
print(Utilts.currency_rates('GBP_2'))

print(Utilts.currency_rates_advanced('USD'))
print(Utilts.currency_rates_advanced('KZT'))
print(Utilts.currency_rates_advanced('eur'))
print(Utilts.currency_rates_advanced('gBp'))
print(Utilts.currency_rates_advanced('GBP_2'))
