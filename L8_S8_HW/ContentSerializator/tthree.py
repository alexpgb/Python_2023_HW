"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""

from pathlib import Path
import csv
import json

SOURCE_DATA_FILE = './L8_S8/l8_s8_t2.json'
TARGET_DATA_FILE = './L8_S8/l8_s8_t2.csv'

HEADER = ['user_level', 'user_id', 'user_name']

DATA_JSON = {}
DATA_FOR_CSV = {}


def read_data(data_file):
    global DATA_JSON
    full_path = Path(data_file).resolve()
    result = False
    if Path(full_path).exists():
        with open(data_file, 'r') as df:
            DATA_JSON = json.load(df)
            result  = True
    return result  



def main():
    if not read_data(SOURCE_DATA_FILE):
        print(f'Не найден файл {SOURCE_DATA_FILE}.')
        return
    with open(TARGET_DATA_FILE, 'w', newline='', encoding='utf-8') as tf:
        csv_write = csv.writer(tf, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writerow(HEADER)
        for user_level, users in DATA_JSON.items():
            for user_id in users:
                csv_write.writerow([user_level, user_id, users[user_id]])
                
    return


if __name__ == '__main__':
    main()
