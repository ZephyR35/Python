#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

#Обработать входной результат и определить в нём имена.
#Определить первую букву имени
#записать первую букву в словарь как ключ, как значение записать список имён
#если первая буква имени в списке имён совпадает с ключом, то оставить имя в списке, иначе удалить
#отсортировать ключи финального словаря по алфавиту

def thesaurus(*names):
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

    for key,val in name_dict.items():
        val_final = []
        i = 0
        while i < len(val):
            if key == val[i][0]:
                val_final.append(val[i])
            else:
                pass
            i+=1
        name_dict[key] = val_final
    keys = sorted(name_dict.keys())
    for key in keys:
        name_dict_final[key] = name_dict[key]

    return name_dict_final
user_input = input('Введите имена через запятую(без пробелов): ')
print(thesaurus(user_input))
