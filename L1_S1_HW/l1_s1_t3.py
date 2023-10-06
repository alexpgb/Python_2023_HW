'''
Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
'''
from random import randint

min_value = 0
max_valie = 10 ** 3
num = randint(min_value, max_valie)
attempt_num = 5
i = 1
print(num)
while True:
    s = input(f'Попытка {i}. Укажите целое число от {min_value} до {max_valie} : ')
    if s == 'q':
        break
    if not s.isdigit():
        print(f'{s} - не является целым числом')
        continue
    v = int(s)
    if not (min_value <= v <= max_valie):
        continue
    if v == num:
        print('Угадал')
        break
    else:
        print(f'{v} {"меньше " if v < num else "больше"} загаданного числа')
    i += 1
    if i > attempt_num:
        print('Количество попыток исчерпано. Не угадал.')
        break

        