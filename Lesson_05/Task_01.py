# Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор.

# генератор вернет число, если его квадрат меньше 200
def iterator_without_yield(n):
    gen_1 = (num for num in range(1,n+1,2) if num**2<200)
    return gen_1
result = iterator_without_yield(20)
