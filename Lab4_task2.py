import csv
import json
# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader] # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding ='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
