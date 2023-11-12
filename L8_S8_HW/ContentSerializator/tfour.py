"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Дополните id до 10 цифр незначащими нулями. 
В именах первую букву сделайте прописной. 
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь. 
Имя исходного и конечного файлов передавайте как аргументы функции.
"""


from pathlib import Path
import json
from sys import argv


SOURCE_DATA_FILE = './L8_S8/l8_s8_t2.csv'
TARGET_DATA_FILE = './L8_S8/l8_s8_t4.json'

HEADER_SOURCE_FILE = ['user_level', 'user_id', 'user_name']

TARGET_DATA = []
SOURCE_DATA = []


def read_data(data_file, source_data):
    full_path = Path(data_file).resolve()
    result = False
    if Path(full_path).exists():
        with open(data_file, 'r') as df:
            for ln, line in enumerate(df):
               line_as_list = list(map(lambda x: x.replace('\"', ''), line[:-1].split('","')))
               if ln == 0:
                    keys = line_as_list
                    continue
               line_as_dict = {k:line_as_list[i] for i, k in enumerate(keys)}
               source_data.append(line_as_dict)
            result  = True
    return result  


def convert_data():
    for i, el in enumerate(SOURCE_DATA):
        target = {}
        target['user_level'] = el['user_level']
        target['user_id'] = el['user_id'].zfill(10)
        if i != 2:
            target['user_name'] = el['user_name'].capitalize()
        if i != 4:
            target['hash'] = hash(el['user_id'] + el['user_name'])
        TARGET_DATA.append(target)
    return


def save_data(data_file, data):
    with open(data_file, 'w', encoding='utf-8') as df:
        json.dump(TARGET_DATA, df, ensure_ascii=False)


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
    convert_data()
    save_data(TARGET_DATA_FILE, TARGET_DATA)
    return


if __name__ == '__main__':
    main()
