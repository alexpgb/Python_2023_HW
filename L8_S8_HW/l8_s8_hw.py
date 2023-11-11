"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
 Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

from sys import argv
from pathlib import Path
import json
import csv
import pickle
from ContentSerializator import extract_header

DIR_DEFAULT = '.'
DATA = []
TARGET_FILE_NAME = 'dir_content'
"""
В эту структуру будем записывать информацию о директории
элементом списка будет словарь с ключами:
type - разновидность объекта каталог/файл/ссылка OBJ_TYPE_DIR=1/OBJ_TYPE_FILE=2/OBJ_TYPE_LINK=3 
parent - полный путь родительского каталога для каталога, полый путь до текущего каталога для файла
size - размер объекта в байтах, для файла, размер всех содержащихся в нем файлов, включая подкаталоги в 
"""
OBJ_TYPE_DIR=1
OBJ_TYPE_FILE=2
OBJ_TYPE_LINK=3
KEY_TYPE = 'type'
KEY_NAME = 'name'
KEY_PARENT = 'parent'
KEY_SIZE = 'size'

def save_to_json(file_name, data: list[dict]):
    with open(file_name, 'w') as f:
        json.dump(data, f, ensure_ascii=True)
    return
  

def save_to_csv(file_name, data: list[dict]):
    header = extract_header(data)
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, header, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, restval='')
        csv_writer.writeheader()
        for el in data:
            csv_writer.writerow(el)
    return


def save_to_pickle(file_name, data: list[dict]):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.DEFAULT_PROTOCOL)
    return


def scrap_dir(dir_name, mask, data: list[dict], dir_size: list[int]):
    """
    При первом вызове функции передаем в нее имя каталога в котром нужно выполнить рекурсивное сканирование.
    Пустой список data в который будут помещаться текущие объекты каталога и подкаталогов
    Список dir_size, содержащий один элемент, к которому будет прибавлен размер объектов, входящих в каталог и список будет
     использоваться как стек для возврата информации о суммарном размере иссследуемого каталога 
    """
    print(dir_name)
    last_dir_sise_el = len(dir_size) - 1
    full_dir_name = Path(dir_name).resolve()
    if Path(full_dir_name).exists():
        dir_content = list(Path(full_dir_name).glob(mask))
        for el in dir_content:
            if el.is_file():
                el_type = OBJ_TYPE_FILE
                size = el.stat().st_size
            elif el.is_symlink():
                el_type = OBJ_TYPE_LINK
                size = el.stat().st_size
            elif el.is_dir():
                el_type = OBJ_TYPE_DIR
                dir_size.append(0)
                scrap_dir(el, mask, data, dir_size)
                size = dir_size.pop()
            else:
                el_type = None
            if el_type:
                dir_size[last_dir_sise_el] += size
                data.append(
                    {
                        KEY_TYPE: el_type
                        ,KEY_PARENT: str(full_dir_name)
                        ,KEY_NAME: str(el.name)
                        ,KEY_SIZE: size
                    }
                )
    return


def main():
    if len(argv) >2:
        _, *target_dir = argv
        target_dir = target_dir[0]
    else:
        target_dir = DIR_DEFAULT
    if not Path(target_dir).resolve().exists():
        print(f'Отсутствует каталог {target_dir}')
    print(Path(target_dir).resolve())
    scrap_dir(target_dir, '*', DATA, [0])
    print('\n'.join(list(map(lambda x: f'{x}', DATA[:100]))))
    save_to_json(Path(target_dir) / '.'.join([TARGET_FILE_NAME, 'json']), DATA)
    save_to_csv(Path(target_dir) / '.'.join([TARGET_FILE_NAME, 'csv']), DATA)
    save_to_pickle(Path(target_dir) / '.'.join([TARGET_FILE_NAME, 'pickle']), DATA)

if __name__ == '__main__':
    main()


from l8s8t4 import read_data as read_data_csv_wo_csv_module
from l8s8t5 import convert_json_to_pickle as file_convert_json_to_pickle
from l8s8t6 import extract_header
from l8s8t7 import convert_data as convert_data_obj_to_pickle

__all__ = ['read_data_csv_wo_csv_module'
        ,'file_convert_json_to_pickle'
        , 'extract_header'
        , 'convert_data_obj_to_pickle']

"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
"""

# ContentSerializator\__inint__.py

from l8s8t4 import read_data as read_data_csv_wo_csv_module
from l8s8t5 import convert_json_to_pickle as file_convert_json_to_pickle
from l8s8t6 import extract_header
from l8s8t7 import convert_data as convert_data_obj_to_pickle

__all__ = ['read_data_csv_wo_csv_module'
        ,'file_convert_json_to_pickle'
        , 'extract_header'
        , 'convert_data_obj_to_pickle']
