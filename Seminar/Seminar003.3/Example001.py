# Дан список чисел. Определите, сколько в нем встречается различных чисел.
import random
#Альтернативный вариант списка
#my_list = [random.randint(0,10) for i in range(20)]

# Обычный список
my_list1 = []
for i in range(20):
    my_list1.append(random.randint(0,10))
print(my_list1)
print(set(my_list1))
print(len(set(my_list1)))

# По приколу
# print(len(set([random.randint(0,10) for i in range(20)])))