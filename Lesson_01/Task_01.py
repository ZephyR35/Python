# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = int(input('Введите секунды: '))
minute = 0
hour = 0
day = 0

while duration > 59:
    minute+=1
    duration = duration - 60
    if minute > 60:
        hour += 1
        minute = 1
        if hour >24:
            day+=1
            hour = 1
if day > 0:
    print(day,'дн',hour,'час',minute,'мин',duration,'сек')
elif hour>0:
    print(hour,'час',minute,'мин',duration,'сек')
elif minute > 0:
    print(minute,'мин',duration,'сек')
else:
    print(duration,'сек')

