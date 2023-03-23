####
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]

list_1 = [i for i in range(1, 101)] # Альтернативная запись

list_1 = [i for i in range(1, 101) if i % 2 == 0]  # Только четные числа

list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # Допустим, вы решили создать пары каждому из чисел (кортежи)

list_1 = [i * 2 for i in range(10) if i % 2 == 0] #умножить значение на 2.