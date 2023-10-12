"""
Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное, шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

def convert_decimal_from_bin_to_hex(value: int, base: int) -> str:
    """
    Выполняется конверсия десятичного положительного числа в систему исчисления с основанием от 2 до 16
    Возвращаемый результат:
        - err_code = 0 - успешное завершение
            - result - результат конверсии;
        - err_code = 1 - неуспешное завершение
            - result = None
    """
    digits = '0123456789abcdef'
    if not isinstance(base, int) or not isinstance(value, int) or not (2 <= base <= len(digits)) or value < 0:
        return 1, None
    dict_digits = {i:digits[i] for i in range(base)}
    prefixes = {
        2:'0b',
        8:'0o',
        16:'0x'
        }
    result = []
    i = 0
    while True:
        result.append(dict_digits[(value // pow(base, i)) % base])
        i += 1
        if pow(base, i) > value:
            break
    if base in prefixes.keys():
        result.append(prefixes[base])
    return 0, ''.join(result[::-1])


def main():
    base_min = 2
    base_max = 16
    control = {
        2: bin,
        8: oct,
        16: hex
        }
    while True:
        v = input('Укажите конвертируемое число (ожидается целое положительное число) : ')
        if v == 'q':
            break
        if not v.isdecimal(): # нам не нужны отрицательные числа поэтому сделаем проверку так
            continue
        v_as_int = int(v)
        while True:
            b = ''
            b = input(f'Укажите основание системы исчисления (ожидается целое число от {base_min} до {base_max}) : ')
            if b == 'q':
                break
            if b.isdecimal() and (base_min <= int(b) <= base_max):
                b_as_int = int(b)
                break
        if b == 'q':
            break
        print(f'Результат: {convert_decimal_from_bin_to_hex(v_as_int, b_as_int)[1]}',\
               (f", проверка: {control[b_as_int](v_as_int)}.") if b_as_int in control.keys() else ".", sep='')
        # if b_as_int in control.keys():
        #    print(f' Контроль: {control[b_as_int](v_as_int)}' )


if __name__ == '__main__':
    main()

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь 
с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""

import math
import fractions


def parse_operand(operand: str):
    operand_as_dict = {}
    if operand[0] == '-':
        operand_as_dict['sign'] = -1
        operand = operand.replace('-','')
    else:
        operand_as_dict['sign'] = 1
        operand = operand.replace('+','')
    if operand.count('/') > 1:
        return 1, f'Ошибка парсинга значения {operand}.', {}
    if '/' not in operand:
        operand_as_dict['numer'] = operand
        operand_as_dict['denom'] = '1'
    else:
        operand_as_dict['numer'], operand_as_dict['denom'] = operand.split('/')
    if operand_as_dict['numer'].isdecimal() and operand_as_dict['denom'].isdecimal():
        return 0, '', {'sign':operand_as_dict['sign'], 
                   'numer': int(operand_as_dict['numer']),
                   'denom': int(operand_as_dict['denom'])}
    else:
        return 1, f'Ошибка парсинга значения {operand}.', {}

def calc_expresson(operand1: dict, operand2: dict, operator: str) -> dict:
    result = {}
    if operator in ('+', '-'):
        lcm = math.lcm(operand1['denom'], operand2['denom'])
        numer1 = operand1['numer'] * int(lcm / operand1['denom'])
        numer2 = operand2['numer'] * int(lcm / operand2['denom'])
        result['numer'] = numer1 * operand1['sign']  \
            + numer2 * operand2['sign'] \
            * (-1 if operator == '-' else 1)
        result['denom'] = lcm
        result['sign'] = -1 if result['numer'] < 0 else 1
        result['numer'] = abs(result['numer'])
    else: #  v_as_list[1] in ('/', '*'):
        result['sign'] = operand1['sign'] * operand2['sign']
        if operator == '*':
            result['numer'] = operand1['numer'] * operand2['numer']
            result['denom'] = operand1['denom'] * operand2['denom']
        else:
            result['numer'] = operand1['numer'] * operand2['denom']
            result['denom'] = operand1['denom'] * operand2['numer']
    return result

def calc_test(operand1: dict, operand2: dict, operator: str ) -> dict:
    result_test = {}
    if operator in ('+', '-'):
        result_test = fractions.Fraction(operand1['sign'] * operand1['numer'], operand1['denom']) \
            + fractions.Fraction(operand2['sign'] * operand2['numer'], operand2['denom'])\
            * (-1 if operator == '-' else 1)
    else: #  v_as_list[1] in ('/', '*'):
        if operator == '*':
            result_test = fractions.Fraction(operand1['sign'] * operand1['numer'], operand1['denom']) \
            * fractions.Fraction(operand2['sign'] * operand2['numer'], operand2['denom']) 
        else:
            result_test = fractions.Fraction(operand1['sign'] * operand1['numer'], operand1['denom']) \
            / fractions.Fraction(operand2['sign'] * operand2['numer'], operand2['denom']) 
    return result_test

def format_result(result: dict) -> str:
    result = f'Результат : {"-" if result["sign"] == -1 and result["numer"] > 0 else "" }'\
            f'{result["numer"]}{"/" + str(result["denom"]) if result["denom"] > 1 and result["numer"] > 0 else ""}.'
    return result


def main():
    operators = ('+', '-', '*', '/')
    e = ''
    while True:
        code = None
        if e != '':
            print(e)
            e = ''
        operand1 = {}
        operand1 = {}
        result = {}
        v = input('Запишите выражение с двумя числами, представленными в виде неправильной дроби (например a/b * -c/d) :')
        if v == 'q':
            break
        v_as_list = v.split()
        if v_as_list[1] not in operators or len(v_as_list[1].strip()) > 1:
            e = 'Ошибка парсинга выражения'
            continue
        code, e, operand1 = parse_operand(v_as_list[0])
        if code > 0:
            continue
        code, e, operand2 = parse_operand(v_as_list[2])
        if code > 0:
            continue
        if operand1['denom'] == 0 or operand2['denom'] == 0:
            continue
        if operand2['numer'] == 0 and v_as_list[1] == '/':
            continue
        result = calc_expresson(operand1, operand2, v_as_list[1])
        result_test = calc_test(operand1, operand2, v_as_list[1])
        gcd = math.gcd(result['numer'], result['denom'])
        result['numer'] = int(result['numer'] / gcd)
        result['denom'] = int(result['denom'] / gcd)
        print(format_result(result))
        print(f'Контроль  : {result_test}.')

if __name__ == '__main__':
    main()

