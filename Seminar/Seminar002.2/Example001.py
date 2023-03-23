import random
days = int(input('Введите количество дней: '))

today = 0
count = 0
z = 0
for _ in range(days):
    today += random.randint(-3,3)
    print(today, end=' ')
    if today >0:
        count+=1
    else:
        if z<count:
            z=count
        count = 0
else:
    if z < count:
        z=count
    count = 0
print(f'Самая долгая оттепель {z}')
