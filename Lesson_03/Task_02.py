#Написать функцию num_translate_adv, которая корректно обработает числительные, начинающиеся с заглавной буквы.
# Если перевод сделать невозможно, вернуть объект None.

numbers = {'one':'один','two':'два','three':'три','four':'четыре','five':'пять','six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять','zero':'ноль'}

number = input('Введите число на английском - ')
def num_translate_adv(number):
    if number[0].isupper():
        number = number.lower()
        result = (numbers.get(number, 'None'))
        return result.capitalize()
    elif number[0].islower():
        number = number.lower()
        result = (numbers.get(number, 'None'))
        return result
print(num_translate_adv(number))