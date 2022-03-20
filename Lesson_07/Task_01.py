#Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок

#|--my_project
#|  |--settings
#|  |--mainapp
#|  |--adminapp
#|  |--authapp


import os
from os.path import join,exists

path_1 = join(".",'my_project')
if not exists(path_1):
    os.mkdir(path_1)
else:
    print('Директория my project уже существует')
directory_lst = ['settings','mainapp','adminapp','authapp']
for elem in directory_lst:
    path_2 = join(path_1,elem)
    if not exists(path_2):
        os.mkdir(path_2)
    else:
        print(f'Директория {elem} уже существует')