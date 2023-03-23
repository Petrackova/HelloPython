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
