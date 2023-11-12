"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара. 
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""

from pathlib import Path
import csv
import pickle
from sys import argv


SOURCE_DATA_FILE = './L8_S8/l8_s8_t4.pickle'
TARGET_DATA_FILE = './L8_S8/l8_s8_t6.csv'

HEADER = []

TARGET_DATA = []
SOURCE_DATA = []


def read_data(data_file):
    global SOURCE_DATA
    full_path = Path(data_file).resolve()
    result = False
    if Path(full_path).exists():
        with open(full_path, 'rb') as df:
               SOURCE_DATA = pickle.load(df)
        result  = True
    return result  


def extract_header(SOURCE_DATA):
    # формируем полный набор ключей, определенных для всех объектов в файле, \
    # т.к. в csv, должны присутствовать все возможные колонки
    header = set()
    for el in SOURCE_DATA:
        header.update(el.keys())
    return list(header)


def save_data(data_file: str, data: list[dict], header: list[str]) -> None:
    with open(data_file, 'w', encoding='utf-8', newline='') as df:
        csv_write = csv.DictWriter(df, header, restval='', dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        for el in data:
            csv_write.writerow(el)
    return


def main():
    global SOURCE_DATA_FILE, TARGET_DATA_FILE
    if len(argv) < 3:
        print('Отсутствуют обязательные параметры.')
        return
    _, SOURCE_DATA_FILE, *TARGET_DATA_FILE = argv
    if not Path(SOURCE_DATA_FILE).resolve().exists():
        print('Отсутствует файл источник')
    TARGET_DATA_FILE = TARGET_DATA_FILE[0]
#    print(Path(TARGET_DATA_FILE).resolve())
    if not Path(TARGET_DATA_FILE).resolve().parent.exists():
        print('Отсутствуют каталог для целевого файла.')
        return
    if not read_data(SOURCE_DATA_FILE, SOURCE_DATA):
        print(f'Не найден файл {SOURCE_DATA_FILE}.')
        return
    HEADER = extract_header(SOURCE_DATA)
    save_data(TARGET_DATA_FILE, SOURCE_DATA, HEADER)
    return


if __name__ == '__main__':
    main()
