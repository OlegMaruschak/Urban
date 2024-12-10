# Домашнее задание по теме "Позиционирование в файле"

import io
from pprint import pprint

def  custom_write(file_name, strings):
    # Если файла нет, то я его создам
    file = open(file_name, 'w', encoding = 'utf-8')
    for string in strings:
        file.write(str(string) + '\n')
    file.close()

    i = 0
    file = open(file_name, 'r', encoding='utf-8')

    tell_ = file.tell()
    line = file.readline().strip()
    i += 1
    cort = (i, tell_)
    dict = {cort:line}

    while line:
        tell_ = file.tell()
        line = file.readline().strip()
        if line != '':
            i += 1
            cort = (i, tell_)
            dict[cort] = line

    file.close()

    return dict


info = [
'Text for tell.',
'Используйте кодировку utf-8.',
'Because there are 2 languages!',
'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# for a, b in dict.items():
#     print(a, b)