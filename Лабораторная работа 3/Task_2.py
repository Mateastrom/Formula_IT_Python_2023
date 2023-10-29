# TODO Напишите функцию find_common_participants
def find_common_participants(first_list_input, second_list_input, split_sign = ','):


    split_input_1 = first_list_input.split(split_sign)
    split_input_2 = second_list_input.split(split_sign)
# [...]->{...} для дальнейшего использования метода intersection
    split_input_1_set = set(split_input_1)
#использование intersection для поиска общих участников и представление в виде списка
    intersection = list(split_input_1_set.intersection(split_input_2))
# сортировка по алфавиту
    intersection.sort()
    return intersection

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

results = find_common_participants(participants_first_group,participants_second_group,'|')


print(results)

#вычисляется требуемый ответ:
#['Петров', 'Сидоров']





participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
#для того чтобы мы могли менять разделители, на входе в строках должны присутствовать желаемые разделители иначе программа не выдаст результат
# например, нельзя было бы использовать "," вместо "|", так как в строках отсутствуют запятые
