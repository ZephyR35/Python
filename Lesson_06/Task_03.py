#Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в json-файл. Проверить сохранённые данные.
import json

persons = open('persons.txt','r',encoding='utf-8')
hobby = open('hobby.txt','r',encoding='utf-8')
final_dict = {}
for person_info in persons:
    person_info = ''.join([letter for letter in person_info if letter.isupper()])
    hobby_info = hobby.readline().replace(',',';')
    if person_info in final_dict.keys():
        pass
    else:
        final_dict[person_info] = hobby_info.rstrip()
print(final_dict)
result = open('result.json','w',encoding='utf-8')
result.write(json.dumps(final_dict))
result.close()
hobby.close()
persons.close()
