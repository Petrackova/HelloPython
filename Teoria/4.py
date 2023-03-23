from bs4 import BeautifulSoup

import requests
import random

def random_word():
    number = random.randint(1,36662)
    word = requests.get(f'https://slovarozhegova.ru/word.php?wordid={number}')
    word = BeautifulSoup(word.text, 'lxml')
    word = (str(word.find('title'))[7:-40])
    if word[-1].isdigit():
        return word[:-1].title()
    elif ' ' in word:
        return word.replace(' ', 'Ё').title()
    else:
        return word.title()

[print(random_word(), end = ' ') for _ in range(10)]