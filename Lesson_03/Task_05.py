# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх заданных списков:

from random import choice
lst_1 = ["автомобиль", "лес", "огонь", "город", "дом"]
lst_2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
lst_3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n,nouns,adverbs,adjectives):
    i = 1
    while i<=n:
        first_word = choice(nouns)
        second_word = choice(adverbs)
        third_word = choice(adjectives)
        result = f'{first_word} {second_word} {third_word}'
        print(result)
        i+=1
get_jokes(4,lst_1,lst_2,lst_3)
