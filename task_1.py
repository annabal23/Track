numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
skip = numbers[:4] + numbers[5:]
new_numbers = numbers[5:]
none = sum(skip) / len(numbers)
numbers[4] = none
modified_list = numbers
print("Измененный список:", modified_list )
