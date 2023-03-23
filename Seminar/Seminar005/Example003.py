'''Задача №35.
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes '''

import random
num = random.randint(0,100)
print(num)
def prost(num):
    for i in range(2, (num//2)+1):
        if num % i == 0:
                return 'Число составное'
    return 'Число простое'
print(prost(num))