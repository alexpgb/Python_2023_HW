'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
'''

while True:
    s = input('Укажите длины сторон треугольника через запятую :')
    if s == 'q':
        break
    m = ''
    acc = 0
    t_sides = s.split(',')    
    if len(t_sides) != 3:
        m = 'Количество чисел не равно трем.'
    else:
        for i in range(len(t_sides)):
            t_sides[i] = t_sides[i].strip()
            if (not t_sides[i].replace('.','').isdigit()) or t_sides[i].count('.') > 1:
                m = f'Значение {t_sides[i]} не является числом'
                break
            else:
                if '.' in t_sides[i]:
                    if len(t_sides[i].split('.')[1]) > acc:
                        acc = len(t_sides[i].split('.')[1])
                t_sides[i] = float(t_sides[i])
    if len(m) > 0:
        print(m)
        continue
    t_sides = [round(el, acc) for el in t_sides]
    print(t_sides)
    t_sides.sort(reverse=True)
    if t_sides[0] >= sum(t_sides[1:]):
            m = f'Сторона треугольника {t_sides[0]} больше суммы двух других.'
    elif t_sides[0] == t_sides[1] and t_sides[0] == t_sides[2]:
        m = f'Треугольник равносторонний.'
    elif  t_sides[0] in t_sides[1:] or t_sides[2] in t_sides[:-1]:
        m = f'Треугольник равнобедренный.'
    else:
        m = f'Просто еще один годный треугольник.'
    print(m)


                