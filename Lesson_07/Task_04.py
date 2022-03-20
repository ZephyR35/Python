#Написать скрипт, который для заданной папки выводит статистику размеров файлов

import os
import os.path

path = os.path.join('.','some_data')
gen_1 = os.scandir(path)
final_dict = {}
i = 0
i_2 = 0
i_3 = 0
i_4 = 0
for elem in gen_1:
    if elem.stat().st_size < 100:
        i += 1
        final_dict['100'] = i
    if 100 < elem.stat().st_size < 1000:
        i_2 += 1
        final_dict['1000'] = i_2
    if 1000 < elem.stat().st_size < 10000:
        i_3 += 1
        final_dict['10000'] = i_3
    else:
        i_4 += 1
        final_dict['остальные'] = i_4


print(final_dict)
print(f'В папке {i} файлов меньше 100 байт; {i_2} файлов от 100 до 1000\n'
      f'{i_3} файлов от 1000 до 10000; {i_4} файлов больше 10000')