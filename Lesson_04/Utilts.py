# Написать свой модуль utils и перенести в него функцию currency_rates и currency_rates_advanced
# Создать скрипт, импортировать в него модуль utils и выполнить несколько вызовов функции currency_rates.
# Убедиться, что ничего лишнего не происходит.


from requests import get, utils
import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)



def currency_rates(currency):
    currency = currency.upper()
    if currency in content:
        curr_idx = content.find(currency)
        temp_str = content[curr_idx:]
        curr_info = temp_str[:content.find('I')]
        value_idx = curr_info.find('Value')
        temp_str_2 = curr_info[value_idx:]
        lst = temp_str_2.split('<')
        result = lst[0][lst[0].find('>')+1:]
        idx = result.find(',')
        begin = result[:idx]
        end = result[idx+1:]
        final_value = float(f'{begin}.{end}')
        return final_value
    else:
        return None

def currency_rates_advanced(currency):
    currency = currency.upper()
    if currency in content:
        curr_idx = content.find(currency)
        temp_str = content[curr_idx:]
        curr_info = temp_str[:content.find('I')]
        value_idx = curr_info.find('Value')
        temp_str_2 = curr_info[value_idx:]
        lst = temp_str_2.split('<')
        result = lst[0][lst[0].find('>')+1:]
        idx = result.find(',')
        begin = result[:idx]
        end = result[idx+1:]
        final_value = float(f'{begin}.{end}')
        date = content[content.find('Date'):content.find('Date') + 17]
        date = date[date.find('"'):]
        date = date[1:-1]
        final_lst = date.split('.')
        for elem in final_lst:
            idx_elem = final_lst.index(elem)
            if elem[0] == '0':
                final_lst[idx_elem] = elem[1:]
        final_date = datetime.date(year=int(final_lst[2]), month=int(final_lst[1]), day=int(final_lst[0]))
        return final_date, final_value
    else:
        return None