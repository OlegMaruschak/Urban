# Домашнее задание по теме "Оператор "with"

import io
from os.path import split
from pprint import pprint

class WordsFinder():
    def __init__(self, *kwargs):
        self.file_names = kwargs

    def get_all_words(self):
        all_words = {}
        # перебираю список файлов
        for aa in self.file_names:
            str_ = []
            # открываю выбранный файл
            with open(aa, encoding='utf-8') as file:
                for line in file:
                    # избавляюсь от пунктуации в строке
                    not_elements = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for not_element in not_elements:
                        line = line.replace(not_element, "")
                    # разбиваю строку на элементы в нижнем регистре
                    str_ = str_ + line.lower().split()
                # добавляю элемент в словарь
                all_words[aa] = str_
        return all_words

    def find(self, word):

        rezult_dict = {}

        my_dict = self.get_all_words()
        for key in my_dict:
            value = my_dict[key]
            num = 0
            for str_ in value:
                num += 1
                if str_ == word.lower():
                    rezult_dict[key] = num
                    break

        return rezult_dict


    def count(self, word):

        rezult_dict = {}

        my_dict = self.get_all_words()
        for key in my_dict:
            value = my_dict[key]
            num = 0
            for str_ in value:

                if str_ == word.lower():
                    num += 1
                    rezult_dict[key] = num

        return rezult_dict


finder2 = WordsFinder('test_file.txt','test_file1.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего