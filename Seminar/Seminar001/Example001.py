
# v = int(input('Введите сколько машина проезжает за день: '))
# day = int(input('Введите расстояние: '))
#
# print(f'Машине потребуется {(day+v-1)//v} дней')

# klass_one = int(input('Введите число парт в первом классе: '))
# klass_two = int(input('Введите число парт во втором классе: '))
# klass_three = int(input('Введите число парт в третьем классе: '))
# summ = (klass_two+1)//2 + (klass_one+1)//2 + (klass_three+1)//2

# print(f'Всего необходимо парт: {summ}')

Vitya_sel = int(input('Введите в какой вагон сел Виктор: '))
number_vagon = int(input('Введите номер вагона: '))
if Vitya_sel == number_vagon:
    print("Мало информации")
else:
    print(f'Всего вагонов: {Vitya_sel+number_vagon-1}')
