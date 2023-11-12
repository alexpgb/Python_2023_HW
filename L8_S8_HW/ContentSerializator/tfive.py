"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
"""
from pathlib import Path
import json
import pickle
from sys import argv

SOURCE_DATA_FILE_EXT = 'json'
TARGET_DATA_FILE_EXT = 'pickle'


def convert_json_to_pickle(source_file, target_file):
    with open(source_file, 'r', encoding='utf-8') as sf:
        data_j = json.load(sf)
    with open(target_file, 'wb') as tf:
        pickle.dump(data_j, tf)
    

def get_files_by_ext(path, mask):
    result = []
    if Path(path).resolve().exists():
        for file in Path(path).resolve().glob(mask):
            if file.is_file():
                result.append(f'{file}')
    return result


def main():   
    if len(argv) >= 2:
        _, SOURCE_PATH = argv
    else:
        SOURCE_PATH ='.\L8_S8'
    files = get_files_by_ext(SOURCE_PATH, '.'.join(['*', SOURCE_DATA_FILE_EXT]))
    for file in files:
        convert_json_to_pickle(file, Path(Path(file).parent / '.'.join([Path(file).stem, TARGET_DATA_FILE_EXT])))


if __name__ == '__main__':
    main()    
