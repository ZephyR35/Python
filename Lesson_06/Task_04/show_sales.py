#Реализовать простую систему хранения данных о суммах продаж булочной.
#Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.


from sys import argv

with open("bacery.csv",'r',encoding='utf-8') as b:
    sales = [sale.strip() for sale in b]
    if len(argv) == 1:
        for sale in sales:
            print(sale)
    elif argv[1]:
        try:
            if argv[2]:
                if int(argv[2]) > len(sales):
                    print(f'Первышено общее количество сумм. Максимальное количество - {len(sales)}')
                else:
                    sales_copy = sales[int(argv[1])-1:int(argv[2])]
                    for sale in sales_copy:
                        print(sale)
        except:
            sales_copy = sales[int(argv[1])-1:]
            for sale in sales_copy:
                print(sale)




