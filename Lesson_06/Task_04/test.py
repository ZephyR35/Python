#from sys import argv


first_param = '2'
second_param = 'new_string'
b = open('bacery.csv','rt+',encoding = 'utf-8')
temp_lst = []

#for line in b:
line = b.readline()
line = line.strip()
if len(line) < 10:
    for elem in line:
        temp_lst.append(elem)
    i = 9
    while len(temp_lst) < i:
        temp_lst.append('.')
    temp_lst.append('\n')
new_line = ''.join(temp_lst)
b.seek(11)
b.write(new_line)
temp_lst.clear()



b.close()