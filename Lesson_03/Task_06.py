# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх заданных списков:

#Добавьте в функцию еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках:
# каждое слово можно использовать только в одной шутке.

import random
lst_1 = ["автомобиль", "лес", "огонь", "город", "дом"]
lst_2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
lst_3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


#repeat = True - повторы разрешены
#repeat = False - повторы запрещены
def get_jokes(n,nouns,adverbs,adjectives,repeat = True):
    i = 1
    lst_copy_1 = nouns[:]
    lst_copy_2 = adverbs[:]
    lst_copy_3 = adjectives[:]
    if repeat == True:
        while i<=n:
            first_word = random.choice(lst_copy_1)
            second_word = random.choice(lst_copy_2)
            third_word = random.choice(lst_copy_3)
            result = f'{first_word} {second_word} {third_word}'
            i+=1
            print(result)
    else:
        while i<=n:
            first_word = random.choice(lst_copy_1)
            lst_copy_1.remove(first_word)
            second_word = random.choice(lst_copy_2)
            lst_copy_2.remove(second_word)
            third_word = random.choice(lst_copy_3)
            lst_copy_3.remove(third_word)
            result = f'{first_word} {second_word} {third_word}'
            i+=1
            print(result)

get_jokes(10,lst_1,lst_2,lst_3)


