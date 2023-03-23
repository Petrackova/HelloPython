"""
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea mshore shells
Output: 13
"""
import string

liter_list = 'She sells sea shells on the sea shore The shells that she sells are sea shells Im sure. So if she sells sea shells on the sea shore Im sure that the shells are sea mshore shells'
liter_list = liter_list.lower()
print(liter_list)
words = liter_list.split()
liter_set = set(words)
result = string.punctuation
print([s.strip(result) for s in liter_set])
print(f'Количесто различный слов: {len(liter_set)}')

punct = string.punctuation
for char in punct:
    liter_list  = liter_list.replase(char, ' ')
print(liter_list)
