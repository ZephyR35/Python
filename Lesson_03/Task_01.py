#Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть объект None.

numbers = {'one':'один','two':'два','three':'три','four':'четыре','five':'пять','six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять','zero':'ноль'}

number = input('Введите число на английском - ')
def num_translate(number):
    number = number.lower()
    return numbers.get(number,'None')
print(num_translate(number))