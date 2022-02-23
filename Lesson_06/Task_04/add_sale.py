from sys import argv

with open("bacery.csv",'a',encoding = 'utf-8') as b:
    try:
        if argv[2]:
            print('Вводите суммы по одной')
    except:
        if argv[1]:
            b.write(argv[1])
            b.write('\n')




