from bs4 import BeautifulSoup

import requests
import random
import re


class OzegWord:
    def __init__(self, number: int = random.randint(1,36622)):
        if 0 > number < 36623:
            raise ValueError
        self.number = number
        self.word : str
        self.description : str
        self.get_word()

    def get_word(self):
        word = requests.get(f'https://slovarozhegova.ru/word.php?wordid={self.number}')
        word = BeautifulSoup(word.text, 'lxml')
        pattern = re.compile("\\s*<p>\\s*<strong>\\s*[\\w]+\\s*</strong>\\s*</p>\\s*.+\\s*</p>.*")
        description = pattern.findall(str(word))[0]
        word = str(word.find('title'))[7:-40]
        description = description[description.rindex(word, 3)+len(word):-6]
        if word[-1].isdigit():
            word = word[:-1].title()
        elif ' ' in word:
            word = word.replace(' ', 'Ё').title()
        else:
            word = word.title()
        self.word = word
        self.description = description

    def __str__(self):
        return self.word

    def get_description(self):
        return f'{self.word.upper()} - {self.description}'

    def __len__(self):
        return len(self.word)

    def get_task(self):
        return self.description.lower().replace(self.word[:-3].lower(), f'{"#" * len(self.word)}')

some_word = OzegWord()
print('#'*len(some_word))
print(some_word.get_description())
print(some_word.get_task())


word = requests.get(f'http://ru.wiktionary.org/wiki/{some_word}')
print(word.text)