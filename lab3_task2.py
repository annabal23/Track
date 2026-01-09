def find_common_participants(str1, str2, split=','):
    intersection = list(set(str1.split(split)).intersection(str2.split(split)))
    intersection.sort()
    return intersection
# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, split= '|')
# TODO Провеьте работу функции с разделителем отличным от запятой
