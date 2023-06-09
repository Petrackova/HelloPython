'''15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9'''

from random import randint
arb = int(input('Введите количество арбузов: '))
max_arb = 1000
min_arb = 30000
while arb!=0:
    ves = randint(1000,30000)
    print(ves, end=' ')
    if ves>max_arb:
        max_arb = ves
    if ves < min_arb:
        min_arb = ves
    arb-=1
print()
print(f'Самый тяжелый арбуз {max_arb} кг')
print(f'Самый легкий арбуз {min_arb} кг')