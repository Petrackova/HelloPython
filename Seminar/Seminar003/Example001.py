# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random

list_1 = list()
n = int(input('Введите число элементов в списке: '))
n = range(n)
count = 0
for i in n: 
    i = random.randint(-5,10)
    list_1.append(i)
print(list_1)      
list_1.sort()
for i in range(len(list_1)):
    if list_1[i - 1] != list_1[i]:
        count += 1
print(count)   

#import random
#Альтернативный вариант списка
#my_list = [random.randint(0,10) for i in range(20)]

# Обычный список
#my_list1 = []
#for i in range(20):
#    my_list1.append(random.randint(0,10))
#print(my_list1)
#print(set(my_list1))
#print(len(set(my_list1)))

# По приколу 
# print(len(set([random.randint(0,10) for i in range(20)])))