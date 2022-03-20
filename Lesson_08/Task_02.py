import re

data = re.compile('(?P<remote_addr>\d{2,3}.\d{1,3}.\d{2,3}.\d{1,3}) - - \[(?P<request_datetime>\d{1,2}\/[A-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\] "(?P<request_type>[A-Z]+) (?P<requested_resource>\/\w+\/\w+ \w+\/\d.\d") (?P<resopnse_code>\d+) (?P<response_size>\d+)')

#Вывод всех данных в кортежах

def log_parse(line):
    lst = data.findall(line)
    try:
        return lst[0]
    except:
        pass


with open('nginx_logs.txt','r',encoding='utf-8') as log_file:
    for line in log_file:
        print(log_parse(line))

#Вывод ip без повторений

def ip_parse(line):
    lst = data.findall(line)
    try:
        return lst[0][0]
    except:
        pass

with open('nginx_logs.txt','r',encoding='utf-8') as log_file:
    temp_lst = []
    for line in log_file:
        ip = ip_parse(line)
        if ip not in temp_lst:
            temp_lst.append(ip)
    for elem in temp_lst:
        print(elem)

