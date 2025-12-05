# TODO Найдите количество книг, которое можно разместить на дискете
value = 1.44 * 1024 * 1024
numbers_of_list = 100
numbers_of_string = 50
numbers_of_symbol = 25
storing = 4
value_first = numbers_of_list * numbers_of_string * numbers_of_symbol * storing
number = int (value // value_first)
print("Количество книг, помещающихся на дискету:", number)
