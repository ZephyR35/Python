# Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.
# Техническое задание:
#
# Для всех нечетных чисел диапазона [1, 1000]
# При решении задачи использовать только арифмитическое операции и циклы.
# Не используем списки, функцию range, преобразование в строку/список.

number = 1
number_cube=0
result = 0
exact_number = 0
number_summ = 0
finish_summ = 0
while number <= 1000:
    if number%2!=0:
        number_cube = number**3
        while number_cube>0:
            exact_number = number_cube%10
            number_cube = number_cube//10
            number_summ = number_summ + exact_number
        if number_summ %7==0:
            finish_summ = finish_summ + number
            print(number,'^3:',number**3,'Cумма цифр куба числа ',number,' = ',number_summ)
        number_summ = 0
    number+=1
print('Сумма чисел, сумма цифр кубов которых делится на 7 - ',finish_summ)





