# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, …)
# и возвращающую курс этой валюты по отношению к рублю
from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(content)
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

# на 44 символа раньше и на 79 символов больше
print(currency_rates('USD'))
print(currency_rates('KZT'))
print(currency_rates('DKK'))
print(currency_rates('EUR'))
print(currency_rates('GBP_2'))
