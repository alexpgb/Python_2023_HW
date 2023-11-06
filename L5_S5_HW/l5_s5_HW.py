"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
def __is_leap_year(year_num: int) -> bool:
    """
    Функция, проверяющая год на високосность 
    Високосный год: делится на 4, но либо делится на 400, либо не делится на 100
    """
    return  year_num % 4 == 0 and (year_num % 400 == 0 or year_num % 100 != 0)
    

def is_date_exists(date_to_be_checked: str) -> bool:
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day, month, year = map(int, date_to_be_checked.split('.'))
    result = False
    if 1 <= year <= 9999:
        if 1 <= month <= 12:
            if 1 <= day <= day_in_month[month - 1] + (1 if month == 2 and __is_leap_year(year) else 0):
                result = True
    return result


"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from sys import argv
import l6_s6_t1_HW_test_date as td

def is_valid_input(inp_str: str) -> bool:
    """Проверяет ввод пользователя на соответствие формату DD.MM.YYYY"""
    date_as_str = inp_str.replace(' ', '')
    result = False
    if len(date_as_str.split('.')) == 3: 
        if 1 <= len(date_as_str.split('.')[0]) <= 2 \
            and 1 <= len(date_as_str.split('.')[1]) <= 2 \
            and 1 <= len(date_as_str.split('.')[2]) == 4:
            if all(map(lambda x: x.isdecimal(), date_as_str.split('.'))):
                result = True
    return result

def main():
    # print(f'{argv = }')
    unpacker = lambda x, y=None, *args : (x, y, args )
    # print(unpacker(argv))
    _, s, *_ = unpacker(*argv)
    # print(f'{s = }')
    # print(f'{s is None = }')
    if not s:
        s = input('Укажите проверяемую дату в формате DD.MM.YYYY :')
    if is_valid_input(s):
        if td.is_date_exists(s):
            resut = f'Дата {s} существует.'
        else:
            resut = f'Дата {s} не существует.'
    else:
        resut = f'Значение {s} указано не корректно.'
    print(resut)

if __name__ == '__main__':
    main()


#######################################################################################
#######################################################################################
    """
    Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
    Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
    Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
    Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
    """

from random import randint

MIN_VALUE_SIDE_OF_SQUARE = 0
MAX_VALUE_SIDE_OF_SQUARE = 7


def is_valid_placement_without_overlapping(existing_options: set[tuple[int]], verified_placement: tuple) -> bool:        
    return verified_placement not in existing_options


def is_valid_placement_queen_do_not_beat_each_other(existing_options: set[tuple[int]], verified_placement: tuple) -> bool:
    """
    Эта функция проверяет текущую позицию
    """
    result = False
    if verified_placement[0] not in map(lambda x: x[0], existing_options) and \
        verified_placement[1] not in map(lambda x: x[1], existing_options): # проверяемая опция не лежит на одной вертикали или горизонали, которые имеют 
        # существующие опции
        for el in  existing_options:  # существующая позиция находится по диагонали от проверяемой
            if abs(verified_placement[0] - el[0]) == abs(verified_placement[1] - el[1]):                
                break
        else: # Проверили все элементы и не словили brake значит проверяемая расстановка не лежит по диагонали от любой из существующих расстановок. 
            result = True 
    return result


def get_random_placement_queen(existing_options: set[tuple[int]], number_of_options: int,
                                is_valid_placement = is_valid_placement_without_overlapping,
                                iter_count: list[int] = [10000]) -> None:
    """
    Напишите функцию в шахматный модуль. 
    Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
    Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
    Возвращает заданное количество комбинаций расстановки фигур
    """
    if number_of_options > pow(MAX_VALUE_SIDE_OF_SQUARE + 1, 2):
        print(f'Заданное число комбинаций {number_of_options} превышает '\
              f'возможное число {pow(MAX_VALUE_SIDE_OF_SQUARE + 1, 2): _} фигур '\
              f'для заданного размера доски {MAX_VALUE_SIDE_OF_SQUARE + 1}x{MAX_VALUE_SIDE_OF_SQUARE+1}.')
        return
    while iter_count[0] > 0:
        iter_count[0] -= 1 #  без учета повторов для принципиального ограничения времении работы.
        i = randint(MIN_VALUE_SIDE_OF_SQUARE, MAX_VALUE_SIDE_OF_SQUARE)
        j = randint(MIN_VALUE_SIDE_OF_SQUARE, MAX_VALUE_SIDE_OF_SQUARE)
        if is_valid_placement(existing_options, (i, j), ):
            existing_options.add((i, j))
            if number_of_options > 1:
                get_random_placement_queen(existing_options, number_of_options - 1, is_valid_placement, iter_count)
            break
    return


def print_placement(existing_options):
    """
    Печать расстановки
    """
    for j in range(MAX_VALUE_SIDE_OF_SQUARE - MIN_VALUE_SIDE_OF_SQUARE + 1):
        coord_points_in_row = sorted(map(lambda x: x[0], filter(lambda x: x[1] == j, existing_options)))
        line = ''.join([f' {"x" if i in coord_points_in_row else " " } |' for i in range(MAX_VALUE_SIDE_OF_SQUARE - MIN_VALUE_SIDE_OF_SQUARE + 1)])
        print(line)

################################################################################################
"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
from l6_s6_t2_3_HW_chess_module import get_random_placement_queen
from l6_s6_t2_3_HW_chess_module import is_valid_placement_without_overlapping, is_valid_placement_queen_do_not_beat_each_other, print_placement

print()
options = set()
get_random_placement_queen(options, 8, is_valid_placement_queen_do_not_beat_each_other)
print()
print(options)
print_placement(options)
