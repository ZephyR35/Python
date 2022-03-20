import os.path
import os


with open('config.yaml','r',encoding='utf-8') as file:
    lst = file.readlines()
    first_line = lst.pop(0).strip()
    main_dir = first_line[:-1] + '_adv'
    os.makedirs(main_dir, exist_ok= True)
    first_level = []
    second_level = []
    third_level = []
    fourth_level = []
    print(lst)
    for elem in lst:
        if elem[2] == '-':
            first_level.append(elem)
        if elem[4] == '-':
            second_level.append(elem)
        if elem[6] == '-':
            third_level.append(elem)
        if elem[8] == '-':
            fourth_level.append(elem)
    print(first_level)
    print(second_level)
    print(third_level)
    print(fourth_level)

#Не хватило мне ни времени, ни мозгов сделать задание, к сожалению. Идея была в том, чтобы определить уровень
#вложенности папок и файлов, раскидать их по спискам, а далее пробегать по файлу, искать соответсвия названий
# и уже определять файлы и папки по нужным путям










