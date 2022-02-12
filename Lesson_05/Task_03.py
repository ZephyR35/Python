# Есть два списка: tutors - имена учеников, groups - названия их классов.
# Необходимо реализовать генератор или функцию-генератор, возвращающий кортежи вида `(<tutor>, <group>)`.

tutors = ['Иван','Степан','Андрей','Илья','Станислав','Сергей']
groups = ['9А','5В','11Б','10А','9Б','8В']
gen_1 = (student for student in tutors)
gen_2 = (grade for grade in groups)
for student in tutors:
    first_elem = next(gen_1)
    try:
        second_elem = next(gen_2)
    except StopIteration:
        second_elem = None
    final_tuple = (first_elem,second_elem)
    print(final_tuple)




