# реквест

import random
import string
print(random.randint(1,100))
print(string.ascii_lowercase)
print(''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(20)]))
print(string.punctuation)

text = '«Instant Karma!» (также известна под названием «Instant Karma! (We All Shine On)»; с англ. — «Мгновенная карма!») — песня британского рок-музыканта Джона Леннона, выпущенная в качестве сингла на лейбле Apple Records в феврале 1970 года. Текст песни выстроен вокруг идеи, что действия влекут последствия незамедлительно. Песня попала в первую пятёрку британских и американских чартов синглов, конкурируя с песней The Beatles «Let It Be» в США, где она стала первым сольным синглом участника группы, разошедшимся миллионным тиражом.'
print(text)
clean_text = []
for word in text.split():
    for char in string.punctuation + '—' + '»' + '«':
        word = word.replace(char, ' ')
    clean_text.append(word)

print(*clean_text)


print(string.printable)

#print('\u00B9')