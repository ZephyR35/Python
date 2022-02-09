#Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
#Иван Иванов,Алексей Петров,Иван Сидоров
def thesaurus_adv(*names):
    person_list = (names[0].split(','))
    print(person_list)
    surname_dict = {}
    name_dict = {}
    final_lst = []
    name_dict_final = {}
    name_list = (names[0].split(','))
    for name in name_list:
        idx = name_list.index(name)
        first_letter = name[0]
        final_lst.append(name)
        if first_letter not in name_dict:
            name_dict[first_letter] = final_lst
        print('Промежуточный словарь: ',name_dict)

    for person in person_list:
        idx = person_list.index(person)
        person = person_list[idx].split(' ')
        name = person[0]
        surname = person[1]
        first_letter_sur = surname[0]
        print(first_letter_sur)
        if first_letter_sur not in surname_dict:
            surname_dict[first_letter_sur] = name_dict
    print(surname_dict)
    for key in surname_dict.keys():      #key - первая буква фамилии
        val_dict = surname_dict[key]     #значение это словарь формата {А:[Иван Иванов,Алексей Петров]}
        for key_1 in val_dict:           #key_1 - первая буква имени
            val = val_dict[key_1]        # значение - список всех людей

user_input = input('Введите Имя и Фамилию: ')
thesaurus_adv(user_input)

#Попытка закончить задание не увенчалась успехом, мне просто времени не хватило.
#Была идея сделать как в прошлом задании. Сделать словарь в котором ключи - первая буква имени, а значение - все перечисленные люди
#Далее создать новый словарь в котором ключи - первая буква фамилии, а значение уже полученный первый словарь.
# Ну а далее выкинуть элементы, из первого словаря, которые не соответсвуют условию и оставить нужные.
# В общем не хватило времени всё реализовать, очень интересно посмотреть как это решается
