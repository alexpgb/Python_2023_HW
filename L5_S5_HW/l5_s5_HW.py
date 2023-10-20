"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import pathlib
import os

def parce_filename_v1(file_name: str) -> tuple [str]:
    return (str(pathlib.Path(file_name).parent), pathlib.Path(file_name).stem, pathlib.Path(file_name).suffix)


def parce_filename_v2(file_name: str) -> tuple [str]:
    return (os.path.dirname(file_name), os.path.splitext(os.path.basename(file_name))[0], os.path.splitext(os.path.basename(file_name))[1])

fn = __file__

print(parce_filename_v1(fn))
print(parce_filename_v2(fn))

"""
 Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
 имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
 В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
 Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ['John', 'Kate', 'Alex']
salaries = [10000, 25000, 15000]
percent_of_bonus = ['30.25%', '25.55%', '10.45%']

bounces = {el[0]: round(el[1] * float(el[2].replace('%', '')) / 100, 2) for el in zip(names, salaries, percent_of_bonus)}

len_field_name = max(map(len, bounces.keys())) + 1
len_field_bounces = len(str(max(bounces.values()))) + 2
print(f'|{"Имя":<{len_field_name}}|{"Бонус":<{len_field_bounces}}|')
print('\n'.join([f'|{el[0]:<{len_field_name}}|{el[1]:>{len_field_bounces}.2f}|' for el in bounces.items()]))

"""
Создайте функцию генератор чисел Фибоначчи
"""


def get_fib(n: int) -> int:
    n0 = 0
    if n < 0:
        # print(None)
        return
    n_cur = 0
    n_next = 1
    for _ in range(n + 1):
        # print(f'{i} : {n_cur}')
        yield n_cur
        n_cur, n_next = n_next, n_cur + n_next
    return

n_max = 10
g = get_fib(n_max)
for n, nf in enumerate(g):
    print(f'{n} : {nf}')
