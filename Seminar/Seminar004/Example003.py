"""Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
За помощью товарищи обратились к Вам, студентам.
Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)

Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)
"""

import random
import string

my_random_text = []

for i in range(random.randint(10,20)):
    word = ''
    for j in range(random.randint(4,8)):
        word += random.choice(string.ascii_lowercase)
    my_random_text.append(word + str(random.choice([',','.','!','?'])
        if random.choice([0,0,0,0,1]) else ''))
print(' '.join(my_random_text))
