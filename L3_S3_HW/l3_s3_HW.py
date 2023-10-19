"""
Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
from collections import Counter

l_1 = [1, 2, 3, 5, 7, 10, 4, 2, 5, 5, 7]

# Вариант #1
d1 = Counter(l_1)
#print(d1)
print([k for k in d1 if d1[k] > 1])

# Вариант #2
print([el for el in set(l_1) if l_1.count(el) > 1])

"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
"""
import requests
from bs4 import BeautifulSoup
import string
import pprint

# В качестве иссточника текста воспользуемся частью статьи о Python
url = 'https://ru.wikipedia.org/wiki/Python'
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
            '   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.request.url)
print(response)
if not response.ok:  # 200..399
    print(f'Ошибка выполнения запроса на странице {url}.')
else:
    soup = BeautifulSoup(response.text, 'lxml')
    text = (''.join([el.text for i, el in \
                    enumerate(soup.find_all('div', class_='mw-parser-output')[1].findChildren(recusive=False)) \
                      if i <200]))\
                .lower()
    # Заменим знаки пунктурации на пробелы и разделим текст на слова 
    text_as_list = ''.join((symb if symb not in string.punctuation else ''  for symb in text)).split()
    words_count = {}
    for el in text_as_list:
        if el in words_count:
            words_count[el] += 1
        else:
            words_count[el] = 1
    # Можно еще сделать через set и count()

    # Т.к. текущая версия Pyton старше, чем 3.6. воспользуемся тем фактом,
    #  что текущая реализация словаря хранит значения ключей в том порядке как их добавили.
    # Сортировка словаря по значению взята отсюда 
    # https://www.geeksforgeeks.org/different-ways-of-sorting-dictionary-by-values-and-reverse-sorting-by-values/
    # Была еще идея поменять местами ключи и значения, но это неправильно, т.к. могут встречаться слова с одинаковой частотой

    # Т.к. в условии написано вернуть 10 .... следовательно нужно, чтобы 
    #  - в результате было 10 значений, даже если 10 - е значение частоты будет встречаться несколько раз
    #  - не обязетельно пересортировывать весь словарь

    i = 1
    max_count = 10    
    words_count_top_n = {}
    # words_count_sorted = sorted(words_count.items(), key = lambda kv: kv[1], reverse=True)
    # pprint.pprint(words_count_sorted)
    for k in (sorted(words_count, key=words_count.get, reverse=True)):
        words_count_top_n[k] = words_count[k]
        if i >= max_count:
            break
        i += 1
    max_len_word = len(max(words_count_top_n, key=len))
    max_len_value = len(str(max(words_count_top_n.values())))
    print('\n'.join([f'{k:<{max_len_word}} : {words_count_top_n[k]:>{max_len_value}}' for k in words_count_top_n]))

"""
Cоздайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

import random

ITEMS = {
        "спички": 10,
        "спальник": 150,
        "дрова": 450,
        "топор": 200,
        "вода": 350,
        "еда": 500,
        "косметичка": 50,
        "ботинки": 100
        }
# print(sum(items.values())) = 1910

def fill_backpack(items: dict, max_weight, how = 'max_items_quantity') -> dict:
    variants_how = ['max_items_quantity', 'random_iems']
    result = {'weight':0 , 'items': []}
    if how not in variants_how:
        how = variants_how[0]
    if how == 'max_items_quantity':
        sorted_items = sorted(ITEMS.keys(), key=ITEMS.get)
    elif how == 'random_iems':
        sorted_items = dict(sorted(({k: random.random() for k in items.keys()}).items(), key=lambda el: el[1])).keys()
        # print(sorted_items)
    for item_name in sorted_items:
        if result['weight'] + items[item_name] > max_weight:
            break
        result['weight'] += items[item_name]
        result['items'].append(item_name) 
    return result

def main():
    min_backpack_weight = min(ITEMS.values())
    max_backpaсk_weight = sum(ITEMS.values())
    while True:
        s = input(f'Укажите вес рюкзака (целое число от {min_backpack_weight} до {max_backpaсk_weight} включительно ) : ')
        if s == 'q':
            break
        if not s.isdecimal() or not (min_backpack_weight <= int(s) <= max_backpaсk_weight):
            continue
        backpacks_weight = int(s)
        backpack = fill_backpack(ITEMS, backpacks_weight, 'max_items_quantity')
        print(f"Наполнение (максимальное количество): {', '.join(backpack['items'])}. Вес: {backpack['weight']}")
        backpack = fill_backpack(ITEMS, backpacks_weight, 'random_iems')
        print(f"Наполнение (случайный порядок): {', '.join(backpack['items'])}. Вес: {backpack['weight']}")

if __name__ == '__main__':
    main()
