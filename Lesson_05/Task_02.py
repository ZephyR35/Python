# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield. Полностью истощить генератор.

def iterator_with_yield(n):
    i = 1
    while i <= n:
        if i %2 != 0:
            yield i
        i+=1
gen_1 = iterator_with_yield(20)
for number_1 in gen_1:
    print(number_1)
print('-----------')
#Усложнение [одна звездочка]:
#С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.

def iterator_with_yield_adv(n):
    i = 1
    while i <= n:
        if i %2 != 0:
            if i**2<200:
                yield i
        i+=1
gen_2 = iterator_with_yield_adv(20)
for number_2 in gen_2:
    print(number_2)
print('-----------')

#Усложнение [две звездочки]:
#С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел.

def iterator_with_yield_adv_2(n):
    i = 1
    summ = 0
    while i <= n:
        if i %2 != 0:
            summ += i
            if i**2<200:
                yield (i,summ)
        i+=1
gen_3 = iterator_with_yield_adv_2(20)
for number_3 in gen_3:
    print(number_3)
print('-----------')