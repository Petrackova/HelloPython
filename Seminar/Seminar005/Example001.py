'''Задача №31.
Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21'''
import random
num = random.randint(-3,15)
def fib(num):
    if num in [1,2]:
        return 1
    elif num == 0:
        return 0
    elif num < 0:
        return False
    return fib(num - 1) + fib(num - 2)

print(f'{num} в ряду Фибоначчи: {fib(num)}') 