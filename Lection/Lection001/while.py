n = 423
summa = 0
while summa > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)


i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
    print(i)


# Пользователь вводит число, необходимо найти минимальный делитель данного числа
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: 
        flag = False
        print(i)
    elif i > n // 2: 
        print(n)
        flag = False
    i += 1