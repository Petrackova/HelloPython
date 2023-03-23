"""
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к cимволам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
#liter_list = input('Введите что-нибудь: ')
#liter_list = list(liter_list)
#print(liter_list)
#liter_set = set(liter_list)
#liter_list2 = list(liter_set)


#for j in range(len(liter_list2)):
#    n = 0
#    for i in range(len(liter_list)):
#        if liter_list[i] == liter_list2[j]:
#            n+=1
#            liter_list.insert(i+1,'_')
#            liter_list.insert(i+2,n)
#print(liter_list)
#print(" ".join(map(str, liter_list)))


# Вариант 2
"""my_string='a a a b c a a d c d d'
print(my_string)
my_string=list(my_string.split())
print(my_string)
temp=[]
for i in my_string:
    if i in temp:
        print(f'{i}_{temp.count(i)}', end=' ')
        temp.append(i)
    else:
        print(i, end=' ')
        temp.append(i)"""


import string
import random
# Вариант 3
all_chars = string.digits+string.ascii_lowercase
my_string = [random.choice(all_chars) for _ in range(30)]
print(my_string)

dict_count = {}

for item in my_string:
    dict_count[item] = dict_count.get(item, -1) + 1
    if dict_count.get(item) > 0:
        print(f'{item}_{dict_count.get(item)}', end=' ')
    else:       
        print(item, end=' ')
