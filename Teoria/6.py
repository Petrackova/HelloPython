from bs4 import BeautifulSoup

import requests
import random
import re

def random_word():
    number = random.randint(1,36662)
    word = requests.get(f'https://slovarozhegova.ru/word.php?wordid={number}')
    word = BeautifulSoup(word.text, 'lxml')

    pattern = re.compile("\\s*<p>\\s*<strong>\\s*[\\w]+\\s*</strong>\\s*</p>\\s*.+\\s*</p>.*")

    description = pattern.findall(str(word))[0]

    word = str(word.find('title'))[7:-40]
    description = description[description.rindex(word, 3)+len(word):-6]

    if word[-1].isdigit():
        return {word[:-1].title():description}
    elif ' ' in word:
        return {word.replace(' ', 'Ё').title():description}
    else:
        return {word.title():description}


rand_word = random_word()
print(rand_word.keys())
print(rand_word.values())