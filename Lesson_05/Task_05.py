#Задан список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке

src = [1,2,8,95,44,12,25,2,8,66,23,44,99]
unique_numbers = set()
temporary = set()
for number in src:
    if number not in temporary:
        unique_numbers.add(number)
    else:
        unique_numbers.discard(number)
    temporary.add(number)
unique_numbers = [number for number in src if number in unique_numbers]
print(unique_numbers)
