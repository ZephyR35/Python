# Реализовать склонение слова «процент» во фразе "N процентов".
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 150:

percent = int(input('Введите проценты: '))
last_number = 0
last_number = percent % 10
if 10<(percent%100)<15:
    print(percent,'процентов')
elif last_number == 1:
    print(percent, 'процент')
elif 2<=last_number<=4:
    print(percent, 'процента')
elif 5<=last_number<=9:
    print(percent, 'процентов')
elif last_number == 0:
    print(percent, 'процентов')
