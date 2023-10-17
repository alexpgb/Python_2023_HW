"""
1. Напишите функцию для транспонирования матрицы
"""

from random import randint


def maxrix_transp(matrix,/):
    """Функция возвращает транспонированную матрицу , полученну на вход
    
    :params args: матрица размером m * n
    :return: матрица размером  n * m
    """
    return tuple(tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))


min_size = 1
max_size = 10
min_value = 0
max_value = 10_000
i = randint(min_size, max_size)
j = randint(min_size, max_size)
print(i, j)
matrix = tuple(tuple(randint(min_value, max_value) for _ in range(i)) for _ in range(j))
matrix_t = maxrix_transp(matrix)
print('Оригинальная матрица :')
print(f'\n'.join(list(f'{el}' for el in matrix)))
print('Транспонированная матрица :')
print(f'\n'.join(list(f'{el}' for el in matrix_t)))

"""
2. Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
 где ключ — значение переданного аргумента, а значение — имя аргумента. 
 Если ключ не хешируем, используйте его строковое представление.
"""
import typing

# f' Хэш {hash(data[i - 1]) if isinstance(data[i - 1], typing.Hashable) else "Объект не хешируемый" }.'\

def get_keyword_arguments_as_dict_with_changed_key_on_value(**kwargs):
    """возвращет словарь состоящий из ключевых параметров, где ключ — значение переданного аргумента, а значение — имя аргумента"""
    return {(kwargs[k] if isinstance(kwargs[k], typing.Hashable) else f'{kwargs[k]}') :k for k in kwargs}


def main():
    print(get_keyword_arguments_as_dict_with_changed_key_on_value(
        a=[1,2,3], b='343241', c=4122.3636, param3 = {'one':1, 'two':2})
        )


if __name__ == '__main__':
    main()

"""
3. Возьмите задачу о банкомате из семинара 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""
OPERATION_TYPE_DEPOSIT = 'deposit'
OPERATION_TYPE_WITHDRAW = 'withdraw'
OPERATION_TYPE_ADDING_INTEREST = 'adding_interest'
OPERATION_TYPE_WITHHOLD_INTEREST = 'withhold_interest'
OPERATION_TYPE_WITHHOLD_TAX = 'withhold_tax'
balance: int = 0 
op_count: int = 1
wealth_tax_threshold: int = 5 * pow(10, 6)
operations_list = []


def main():
    global balance
    global op_count
    while True:
        s = input('Выберите операцию (1 - пополнить; 2 - снять; 3 - выход) : ')
        if s not in ('1', '2', '3'):
            continue
        if get_balance() > wealth_tax_threshold:
            amount_as_int = calc_percent(get_balance(),0.9) 
            reduce_balance(amount_as_int)
            save_operation_info_to_list(OPERATION_TYPE_WITHHOLD_TAX, amount_as_int, -1, get_balance())
        if s == '1':
            deposit()
        elif s == '2':
            withdraw()
        elif s == '3':
            break
        else:
            continue
        print_balance(get_balance())        
    print('Список операций')
    print(f'\n'.join([f'{el}' for el in operations_list]))


def get_balance() -> int:
    """Возвращает значение баланса

    :rtype: int
    :return: величина баланса в копейках
    """
    return balance


def increase_balance(amount: int) -> None:
    """Увеличивает значение баланса на переданную величину
    
    :param amount:  величина увеличения баланса в копейках
    :type amount: int

    :return : None
    """
    global balance
    balance += amount


def reduce_balance(amount: int) -> None:
    """Уменьшает значение баланса на переданную величину
    
    :param amount:  величина уменьшения баланса в копейках
    :type amount: int

    :return : None
    """
    global balance
    balance -= amount


def print_balance(balance: int) -> None:
    """Приводит переданное значение баланса к целому значению денежных единиц и печатает его
    
    :param balance: величина которую нужно вывести на печать в копейках
    :type balance: int

    :return : None
    """
    print(f'На счете {balance/100: .2f} ед.')       


def get_op_count() -> int:
    """Возвращает счетчик операций
    
    :return : int - текущее значения счетчика операций
    """
    return op_count


def increase_op_count_by_one() -> None:
    """Увеличивает счетчик операций на 1
    
    :return : None
    """
    global op_count
    op_count += 1


def deposit() -> None:
    """Реализует операцию вненсение денег"""
    while True:
        v = input('Укажите сумму пополнения кратная 50 ед :')
        try:
            amount_as_int = int(v) * 100
        except ValueError:
            continue
        if not amount_as_int % 5000 == 0:
            print(f'Сумма должна быть кратна 50 ед.')
            continue
        increase_balance(amount_as_int)
        save_operation_info_to_list(OPERATION_TYPE_DEPOSIT, amount_as_int, +1, get_balance())
        if get_op_count() % 3 == 0:
            amount_as_int = calc_percent(get_balance(), 0.03)
            increase_balance(amount_as_int)
            save_operation_info_to_list(OPERATION_TYPE_ADDING_INTEREST, amount_as_int, +1, get_balance())
        increase_op_count_by_one()
        break
    

def withdraw() -> None:
    """ Реализует операцию снятия денег """
    while True:
        v = input('Укажите сумму снятия кратная 50 ед :')
        try:
            amount_as_int = int(v) * 100
        except ValueError:
            continue
        if not amount_as_int % 5000 == 0:
            print(f'Сумма должна быть кратна 50 ед.')
            continue
        withdrawal_percent_as_int = calc_percent(get_balance(), 0.015)
        # но не менее 30 и не более 600 у.е
        if withdrawal_percent_as_int < 3000:
            withdrawal_percent_as_int = 3000
        if withdrawal_percent_as_int > 60000:
            withdrawal_percent_as_int = 60000
        if get_balance() < amount_as_int + withdrawal_percent_as_int:
            print(f'Недостаточно средств на счете.')
            break
        reduce_balance(amount_as_int)
        save_operation_info_to_list(OPERATION_TYPE_WITHDRAW, amount_as_int, -1, get_balance())
        reduce_balance(withdrawal_percent_as_int)
        save_operation_info_to_list(OPERATION_TYPE_WITHHOLD_INTEREST, withdrawal_percent_as_int, -1, get_balance())
        if get_op_count() % 3 == 0:
            increase_balance(calc_percent(get_balance(), 0.03))
            save_operation_info_to_list(OPERATION_TYPE_ADDING_INTEREST, amount_as_int, +1, get_balance())
        increase_op_count_by_one()
        break


def calc_percent(base: int, percent: float) -> int: 
    """Возвращает сумму процентов от переданного числа
    
    :param base: база для расчета процентов
    :type base: int
    :param float: процентное число в долях
    :type percent: float
    
    :rtype: int
    :return : величина рассчитанных процентов
    """
    return int(round(base * percent, 0))


def save_operation_info_to_list(operation_type: str, amount: int, sign: int, total_balance: int) -> None:
    """Добавляет информацию об операции в список операций

    :param operation_type: - тип операции ['withdraw', 'deposit']
    :type operation_type: str
    :param amount: сумма операции в копейках
    :type amount: int
    :param sign: знак операции
    :type sign: int [-1, 1] 
    :param total_balance: величина баланса после выполнения операции в копейках
    :type total_balance: int 

    :return: None
    """
    operations_list.append({
        'type':operation_type,
        'amount': abs(amount),
        'DK': 'DR' if sign < 0 else 'KR',
        'total_balance': total_balance,        
    })


if __name__ == '__main__':
    main()
