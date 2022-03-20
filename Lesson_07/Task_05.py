import os.path
import json

path = os.path.join('.','some_data_adv')

gen_1 = os.scandir(path)
i = 0
i_2 = 0
i_3 = 0
i_4 = 0
final_dict = {}
lst = []
lst_2 = []
lst_3 = []
for file in gen_1:
    file_name = file.name
    file_type = file_name[file_name.find('.')+1:]
    file_size = file.stat().st_size
    if file_size < 1000:
        i+=1
        if file_type not in lst:
            lst.append(file_type)
        final_dict[1000] = [i,lst]
    if file_size < 10000:
        i_2+=1
        if file_type not in lst_2:
            lst_2.append(file_type)
        final_dict[10000] = [i,lst_2]
    if file_size < 100000:
        i_3+=1
        if file_type not in lst_3:
            lst_3.append(file_type)
        final_dict[100000] = [i,lst_3]
print(final_dict)
result = open('summary.json','w',encoding='utf-8')
result.write(json.dumps(final_dict))
result.close()


