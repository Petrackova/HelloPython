my_list = [1,2,3,2,2]
print(my_list)
#my_list.remove(2)  # Удаление первого попавшегося элемента
#my_list.remove(2)
#my_list.remove(2)
#print(my_list)
my_list.append(5) #добавление числа в конец
print(my_list)
my_list.pop(2) # удаление числа по индексу
print(my_list)
print(my_list.pop(2)) # удаленный элемент по индексу
my_list.insert(0 , 'start') #  вставка с перемещением
print(my_list)
my_list = my_list + [6,5,7]
print(my_list)
print(my_list.index(2))

#Копирование меняется везде
new_list = my_list
print(my_list)
print(new_list)
my_list.append(6)
print(my_list)
print(new_list)

# Копирование
new_list = my_list.copy()
print(my_list)
print(new_list)
new_list.append(7)
print(my_list)
print(new_list)

# Из строки в список
string = 'Привет'
print(string)
string = list(string)
print(string)




#list = [] # Список
#tuple = ()  # неизменяемый тип данных Кортеж
#set = {}  # множества
#dict = {key:value}  +  #словарь

my_list = [1,2,3,4,3]
print(my_list)
item = my_list.pop(2)
my_list.append(item)

print(my_list)



my_dict = {1:'one', 2:'two', 3:'three'}
my_dict[4] = 'four'
my_dict.setdefault(5,'five')
print(my_dict)
print(my_dict.get(1))


for i in my_dict.values():
    print(i)

