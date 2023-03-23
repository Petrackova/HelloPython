#СЛОВАРИ

#d = {}
#d = dict()

#d['q'] = 'qwerty'
#print(d)
#d['w'] = 'werty'
#print(d['q'])

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print(item)  #Вывод только ключей
    print('{}: {}'.format(item, dictionary[item]))
for (k,v) in dictionary.items():
    print(k,v)
# up: ↑
# down: ↓
# right: →
print(dictionary.items()) #кОРТЕЖ
dictionary[896] = 94533 # ПРосто добавиться в словарь
print(dictionary)