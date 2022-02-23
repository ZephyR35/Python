#[Задача со звездочкой]: усложненный вариант задания 4.
# Добавить возможность редактирования данных при помощи отдельного скрипта.

#from sys import argv
argv_lst = [0,'2','new_string']
def update_sales(number_of_string,new_string):
    with open('bacery.csv','r+',encoding = 'utf-8') as b:
        line = b.readline().strip()
        temp_lst = []
        for elem in line:
            temp_lst.append(elem)

        length = 10
        while len(temp_lst) < length:
            temp_lst.append(' ')
        temp_lst.append('\n')

        new_line = ''.join(temp_lst)
        line = line.replace(line, new_line)
        print(b.tell())
        tail = b.readlines()
        line = line.replace(line, new_line)


update_sales('2','new_string')