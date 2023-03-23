# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]
import random

list_1 = list()
n = int(input('Введите число элементов в списке: '))
k = int(input('Введите число для сдвига: '))
n = range(n)
p = range(k)
for i in n: 
    i = random.randint(-5,10)
    list_1.append(i)
print(list_1)
if k < 0:
    p = range(abs(k))
    for i in p:
        list_1.append(list_1.pop(0))
else:
    for i in p:
        list_1.insert(0, list_1.pop())
print(list_1)



list_1 = [1,2,3,4,5]
list_2 = [0,0,0,0,0]

for i in range(len(list_1)):
    new_pos = (i+k-1) % len(list_1)
    list_2[new_pos] = list_1[i]

print(f'{list_1} -> {list_2}')
    
#Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
import random

my_list = [random.randint(0,10) for i in range(10)]
print(my_list)
K = int(input("Введите число К: "))

for i in range(K):
    temp = my_list.pop(len(my_list)-1)
    my_list.insert(0,temp)

print(my_list)

print(my_list[-K:] + my_list[:-K])
