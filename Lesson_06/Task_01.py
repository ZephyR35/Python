#url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
#Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt


with open('nginx_logs.txt','r',encoding='utf-8') as file_1:
    final_lst = []
    for elem in file_1:
        str = file_1.readline()
        remote_addr = str[:str.find(' ')]
        tag_open = str.find('GET')
        if tag_open == -1:
            tag_open = str.find('HEAD')
        tag_close = str.find(' ',tag_open)
        request_type = str[tag_open:tag_close]
        tag_open = str.find('/downloads')
        tag_close = str.find('"',tag_open)
        requested_resource = str[tag_open:tag_close]
        final_lst.append((remote_addr,request_type,requested_resource))
    print(final_lst)