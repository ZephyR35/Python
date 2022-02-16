prices = [25.12,252.5,90,199.9,651.99,955,1000.32,2125.35]

#вывод отредактированных цен
for price in prices:
    cent = price - int(price)
    cent = round(cent,2)
    cent = cent*100
    cent = int(cent)
    cent = str(cent)
    if len(cent) == 1:
        cent = f'0{cent}'
        print(f'{int(price)} руб {cent} коп', end = ',')
    else:
        print(f'{int(price)} руб {cent} коп', end = ',')
print('---------',end = '\n')

#Сортировка списка по возрастанию, доказательство неизменности его id
print('Список - ',prices)
print('id списка - ',id(prices))
prices.sort()
print('Отсортированный список по возрастанию - ',prices)
print('id списка - ',id(prices))
#Сортировка списка по убыванию, доказательство неизменности его id
print('Список - ',prices)
print('id списка - ',id(prices))
prices.sort(reverse=True)
print('Отсортированный список по убыванию - ',prices)
print('id списка - ',id(prices))

# Вывод 5 максимальных цен
i = 0
prices_copy = prices[:]
while i <5:
    max_price = max(prices_copy)
    prices_copy.remove(max_price)
    print(max_price)
    i+=1