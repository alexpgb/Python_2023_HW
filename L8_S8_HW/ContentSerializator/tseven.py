"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Распечатайте его как pickle строку.
"""

from pathlib import Path
import pickle
from sys import argv


SOURCE_DATA_FILE = ['./L8_S8/l8_s8_t6.csv']

TARGET_DATA = []
SOURCE_DATA = []


def convert_data(source_data: list[list[str]]) -> bytes:
    return pickle.dumps(source_data, protocol=pickle.DEFAULT_PROTOCOL)


def print_data(data) -> None:
    print(f'{data}')
    return




def main():
    global SOURCE_DATA_FILE
    # if len(argv) < 2:
    #     print('Отсутствуют обязательные параметры.')
    #     return
    # _, *SOURCE_DATA_FILE = argv
    SOURCE_DATA_FILE = SOURCE_DATA_FILE[0]
    if not Path(SOURCE_DATA_FILE).resolve().exists():
        print('Отсутствует файл источник')
#    print(Path(TARGET_DATA_FILE).resolve())
    if not read_data(SOURCE_DATA_FILE, SOURCE_DATA):
        print(f'Не удалось прочитать файл {SOURCE_DATA_FILE}.')
        return
    TARGET_DATA = convert_data(SOURCE_DATA)
    print_data(TARGET_DATA)
    return


if __name__ == '__main__':
    main()
