lst_1 = ['приблизительно','в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']


def add_mark_after_number(list):
    for string in lst_1:
        if  '+' in string:
            idx = lst_1.index(string)
            lst_1.insert(idx + 1, '"')
        elif '-' in string:
            idx = lst_1.index(string)
            lst_1.insert(idx + 1, '"')
        elif string.isdigit():
            idx = lst_1.index(string)
            lst_1.insert(idx+1,'"')

def add_zero(list):
    for string in lst_1:
        if string[0] == '+' in string:
            idx = lst_1.index(string)
            if len(string) <= 2:
                string = f'{string[0]}0{string[1:]}'
            lst_1[idx] = string
        elif string[0] == '-' in string:
            idx = lst_1.index(string)
            if len(string) <= 2:
                string = f'{string[0]}0{string[1:]}'
            lst_1[idx] = string
        elif string.isdigit():
            idx = lst_1.index(string)
            if len(string) == 1:
                string = f'0{string}'
            lst_1[idx] = string
add_mark_after_number(lst_1)
lst_1.reverse()
add_mark_after_number(lst_1)
lst_1.reverse()
print(lst_1)
add_zero(lst_1)
print(lst_1)


# Формирование строк из элементов списка с кавычками без пробелов

i = 0
while i<len(lst_1):
    result = lst_1.pop(i)
    if result == '"':
        pass
    elif result[0] == '+':
        result = f'"{result}"'
        print(result, end = ' ')
    elif result[0] == '-':
        result = f'"{result}"'
        print(result, end=' ')
    elif result.isdigit():
        result = f'"{result}"'
        print(result, end = ' ')
    else:
        print(result, end=' ')
# не придумал как реализовать запись кавычек без пробелов. Была идея пробегать по списку циклом до обнаружения кавычек,
# далее записывать в строку с пробелами всё что было до кавычек, потом создать сроку в которой будет записано всё что находится между кавычек,
# только уже без пробелов. И таким образом пройтись по всему списку, выделить из него отдельные строки и просто сложить их, но как-то не вышло.
# так что оставляю вариант вывода всего результата в одну строку, в которой каждый элемент является отдельно взятой строкой.