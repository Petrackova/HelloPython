"""По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
Input: 5
Output: 120"""
while True:
    if num.isdigit():
        num = abs(int(num))
        break
    else:
        print('Введите целое число')
    num_0 = 1
    if num < 0:
        print('Число меньше нуля')
    else:
        while num > 0:
            num_0=num * num_0
            num=num-1
        print(f'Фактариал равен: {num_0}')
