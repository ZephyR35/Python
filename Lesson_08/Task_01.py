#Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен
# из email адреса и возвращает их в виде словаря.

import re

def email_parse(email_adress):
    data = re.compile('(?P<username>[-.+_\w]+)(@)(?P<domain>([-.a-z0-9]+)\.[a-z]+)')
    lst = data.findall(email_adress)
    if not len(lst):
        raise ValueError('Неверный email адрес')
    final_dict = {'username':lst[0][0],'domain':lst[0][2]}
    return final_dict
print(email_parse('someone@geek-brains.com'))