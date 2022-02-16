# Есть два списка: tutors - имена учеников, groups - названия их классов.
# Необходимо реализовать генератор или функцию-генератор, возвращающий кортежи вида `(<tutor>, <group>)`.

lst_1 = ['Иван','Степан','Андрей','Станислав','Виктор','Елена','Екатерина']
lst_2 = ['9А','5В','11Б','10Б','8В','9Б','11А']
def tuple_gen(students,groups):
    idx = 0
    while idx < len(students):
        student = students[idx]
        try:
            group = groups[idx]
            final_tuple = (student, group)
            yield final_tuple
        except IndexError:
            group = None
            final_tuple = (student, group)
            yield final_tuple
        idx+=1
final_gen = tuple_gen(lst_1,lst_2)
for elem in final_gen:
    print(elem)
next(final_gen)