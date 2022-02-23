#[Задача со звездочкой]: усложненный вариант задания 1.
# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Спамер — это клиент, отправивший больше всех запросов.

def spamer_find(file_name,n): #file_name - имя файла в котором будет идти поиск спамера, n - необходимое количество спамеров
    with open(file_name,'r',encoding='utf-8') as file_1:
        i = 0
        spam_dict = {}
        for elem in file_1:
            str = file_1.readline()
            remote_addr = str[:str.find(' ')]
            if remote_addr in spam_dict.keys():
                spam_dict[remote_addr]+=1
            else:
                spam_dict[remote_addr] = 1
    i = 0
    final_dict = {}
    while i<n:
        spamer_ip = max(spam_dict,key = spam_dict.get)
        requests_count = spam_dict[spamer_ip]
        final_dict[spamer_ip] = requests_count
        del spam_dict[spamer_ip]
        i+=1
    return final_dict
print('Ключ словаря - IP спамера, Значение - количество запросов')
print(spamer_find('nginx_logs.txt',3))





