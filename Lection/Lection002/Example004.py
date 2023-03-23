# МНОЖЕСТВА


colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red') # Не добавиться
print(colors) # {'red', 'green', 'blue'}
colors.add('gray') # Добавиться в лююбое место
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red') #удаление
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok пропуск удвления если элемента нет
print(colors) # {'green', 'blue','gray'}
colors.clear() # { } полностью удаление множества
print(colors) # set() 

q = set()

# Операции со множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, объединение
i = a.intersection(b) # i = {8, 2, 5} пересечение
dl = a.difference(b) # dl = {1, 3} вычитание из а б
dr = b.difference(a) # dr = {13, 21} вычитани6е из б в а
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} 1. пересечение 2. Разность 3. Объединение

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})