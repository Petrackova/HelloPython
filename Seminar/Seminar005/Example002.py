'''Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1'''

import random

list_1 = list()
n = int(input('Введите число элементов в списке: '))
n = range(n)
count = 0
for i in n: 
    i = random.randint(1,5)
    list_1.append(i)
print(list_1)
for i in range(len(list_1)):
    if list_1[i] == 4 or list_1[i] == 5:
        list_1[i] = 1
print(list_1)