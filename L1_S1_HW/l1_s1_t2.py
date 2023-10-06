'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: 
    “Число является простым, если делится нацело только на единицу и на себя”.
 Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''
min_value = 0
max_value = 10 ** 5 
not_prime_number = [0, 1]
while True:
    s = input(f'Укажите целое число от {min_value} до {max_value:,} включительно :')
    if s == 'q':
        break
    if not s.isdigit() or not (min_value <= int(s) <= max_value):
        continue
    v = int(s)
    if v in not_prime_number:
        m = f'Число {v} не являетя простым.'
    else:
        print(round(v ** 1/2 ,0) + 1)
        for i in range(2, int(round(v ** 1/2 ,0) + 1)):
            if v % i == 0:
                m = f'Число {v} составное.'
                break
        else:
            m = f'Число {v} простое.'
    print(m)

